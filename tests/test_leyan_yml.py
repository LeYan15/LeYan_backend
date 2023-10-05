# import os

# from .conftest import root_dir


# class TestWorkflow:
#    def test_workflow(self):
#        leyan_workflow_basename = "leyan_workflow"
#        yaml = f"{leyan_workflow_basename}.yaml"
#        yml = f"{leyan_workflow_basename}.yml"
#        filename = (
#            yaml if os.path.exists(os.path.join(root_dir, yaml)) else yml
#        )
#
#        if os.path.isfile(os.path.join(root_dir, filename)):
#            with open(os.path.join(root_dir, filename), "r") as f:
#                leyan = f.read()


#        assert (
#            re.search(r"on:\s*push:\s*branches:\s*-\smaster", leyan)
#            or "on: [push]" in leyan
#            or "on: push" in leyan
#        ), f"Проверьте, что добавили действие при пуше в файл {filename}"

#        assert "pytest" in leyan, f"Проверьте, что добавили pytest
# в файл {filename}"
#        assert (
#            "appleboy/ssh-action" in leyan
#        ), f"Проверьте, что добавили деплой в файл {filename}"
