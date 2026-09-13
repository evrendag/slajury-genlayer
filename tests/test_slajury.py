import json
ELIGIBLE=json.dumps({"scope_match":True,"customer_impact":"CONFIRMED","exclusion_category":"NONE","primary_reason":"SLO_BREACH","qualifying_minutes":459,"unsupported_minutes":0,"evidence_grade":"HIGH","summary":"Official incident timing and customer monitoring confirm the same regional connectivity loss."})
PARTIAL=json.dumps({"scope_match":True,"customer_impact":"PARTIAL","exclusion_category":"NONE","primary_reason":"SLO_BREACH","qualifying_minutes":75,"unsupported_minutes":45,"evidence_grade":"HIGH","summary":"Customer monitoring supports only seventy-five minutes of the official incident interval."})
MISSING=json.dumps({"scope_match":True,"customer_impact":"UNCONFIRMED","exclusion_category":"NONE","primary_reason":"MISSING_CUSTOMER_EVIDENCE","qualifying_minutes":0,"unsupported_minutes":459,"evidence_grade":"LOW","summary":"The incident is official, but no reliable evidence proves impact on this customer."})
def deploy(direct_deploy):return direct_deploy("contract.py",sdk_version="v0.2.12")
def create(c,region="europe-west3-c"):c.create_claim("Google Cloud","Compute Engine","Single Instance",region,"2024-10","https://status.example/incident","https://monitor.example/log",1729670400,1729697940)
def pages(vm):vm.mock_web(r".*status\.example.*",{"status":200,"body":"Official outage in europe-west3-c lasted 459 minutes."});vm.mock_web(r".*monitor\.example.*",{"status":200,"body":"Customer instance connectivity failed for 459 minutes."})
def test_invalid_interval(direct_vm,direct_deploy):
 c=deploy(direct_deploy)
 with direct_vm.expect_revert("Invalid incident"):c.create_claim("Cloud","Compute","Tier","region","2024-10","https://a.example/x","https://b.example/y",2,1)
def test_create(direct_deploy):c=deploy(direct_deploy);create(c);assert c.get_claim(0).status=="PENDING"
def test_eligible_credit_is_deterministic(direct_vm,direct_deploy):
 pages(direct_vm);direct_vm.mock_llm(r".*",ELIGIBLE);c=deploy(direct_deploy);create(c);c.audit_claim(0);r=c.get_receipt(0);assert r.status=="CREDIT_RECOMMENDED";assert r.recommended_credit_bps==5000;assert direct_vm.run_validator()is True
def test_partial(direct_vm,direct_deploy):
 pages(direct_vm);direct_vm.mock_llm(r".*",PARTIAL);c=deploy(direct_deploy);create(c);c.audit_claim(0);assert c.get_receipt(0).status=="PARTIAL_CREDIT_RECOMMENDED"
def test_missing_customer_evidence_fails_closed(direct_vm,direct_deploy):
 pages(direct_vm);direct_vm.mock_llm(r".*",MISSING);c=deploy(direct_deploy);create(c);c.audit_claim(0);assert c.get_receipt(0).status=="MANUAL_REVIEW"
def test_second_audit_rejected(direct_vm,direct_deploy):
 pages(direct_vm);direct_vm.mock_llm(r".*",ELIGIBLE);c=deploy(direct_deploy);create(c);c.audit_claim(0)
 with direct_vm.expect_revert("Already finalized"):c.audit_claim(0)
