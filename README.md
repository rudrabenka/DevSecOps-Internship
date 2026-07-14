# DevSecOps 

## Environment Setup

### Installed Tools
- Git 2.53.0
- Docker 29.0.1
- OpenJDK 17.0.19
- kubectl v1.36.2
- Helm v3.21.2
- Minikube v1.38.1
- Jenkins

## Kubernetes Verification
- Minikube cluster created successfully.
- kubectl get nodes: Successful
- kubectl cluster-info: Successful

## Jenkins
- Jenkins installed successfully.
- Admin user created.
- Suggested plugins installed.
- Git Plugin installed.
- Docker Plugin installed.
- Pipeline Plugin installed.

## Status
# Day‑2: Jenkins Pipeline Setup

## Objective
To automate build and test stages using Jenkins and GitHub integration.

## Steps Performed
1. Created a Jenkinsfile with two stages:
   - **Build:** Installed dependencies from `requirements.txt`.
   - **Test:** Executed `pytest` on `test_app.py`.
2. Committed and pushed Jenkinsfile to GitHub.
3. Configured Jenkins to pull code from GitHub automatically.
4. Ran the pipeline successfully — all stages passed.

## Verification
- Jenkins console output showed: `1 passed in 0.01s`.
- Pipeline ended with `Finished: SUCCESS`.
- Jenkins dashboard displayed blue success indicators.

## Deliverables
- Jenkinsfile committed in GitHub.
- Pipeline success screenshots captured.
- README updated with Day‑2 documentation.

## Outcome
The CI pipeline is fully functional and integrated with GitHub.

Day 2 Completed Successfully.




## Day-3: Docker Setup

### Steps Executed
1. Created optimized multi-stage Dockerfile with comments explaining each instruction.
   ```bash
   docker build -t myapp:1.0 .
docker run -p 5000:8080 myapp:1.0
 
docker ps
Documented Dockerfile instructions and container run in README

.
### Day‑4 SonarQube Analysis
- **Before Fixes:** 2 Bugs, 1 Vulnerability, 3 Code Smells
- **After Fixes:** 0 Bugs, 0 Vulnerabilities, 0 Code Smells
- **Resolved Issues:**
  - Removed hardcoded password
  - Fixed SQL injection risk (used parameterized query)
  - Added zero‑division check
  - Validated `None` values before access
  - Removed duplicate code
- **Quality Gate:** Passed ✅
