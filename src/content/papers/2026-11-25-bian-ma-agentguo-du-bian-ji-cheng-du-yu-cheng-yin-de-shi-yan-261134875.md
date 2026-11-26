---
title: How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded
  Edits in Repository-Level Agent Patches
title_zh: 编码Agent过度编辑程度与成因的实证研究及Delta残差归因方法
authors:
- Aakash Goel
- Benjamin Steenhoek
- Yu Hu
affiliations:
- Microsoft
arxiv_id: '2611.34875'
url: https://arxiv.org/abs/2611.34875
pdf_url: https://arxiv.org/pdf/2611.34875
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 编码任务归因与性能优化
tags:
- CodingAgent
- OverEditing
- DeltaResidueAttribution
- SWE-bench
- AgentEvaluation
one_liner: 提出Delta残差归因方法量化编码Agent补丁不必要编辑，拆解成因并给出优化方案
practical_value: '- 可复用DRA归因思路：对Agent生成的内容（如推荐文案、商品标题改写、运营策略补丁）按粒度拆分，通过回退验证+业务效果校验判断每个修改单元是否必要，过滤冗余改动

  - Agent生成内容后处理可参考该方案：优先用生成内容自审核（让Agent自行justify每个改动）保障精度，再结合业务现有规则/测试用例做剪枝提升召回，平衡冗余去除率和有效内容保留率

  - Agent性能评估不能只看成功率：新增「必要精度NP」类指标，避免模型为提升成功率生成大量冗余内容，推高后续人工审核/上线成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
编码Agent生成的补丁普遍远大于开发者提交的版本，被广泛认为存在过度编辑问题，但仅靠补丁大小无法区分额外改动是否必要、属于什么类型、来自哪步流程，同时现有评估仅关注任务成功率，导致大量高通过率补丁因冗余过高难以落地，亟需可量化的过度编辑评估与归因方法。

## 方法关键点
- 提出Delta Residue Attribution (DRA) 框架：重放Agent全轨迹，将最终补丁拆分为可独立回退的单元，追溯每个单元的生成步骤，通过回退单元重跑测试判断其必要性，定义必要精度NP（有效单元占总单元比例）作为核心量化指标。
- 对单元按类型（代码/测试/文档/配置）分类，将生成步骤划分为DEBUG/FIX/CLEANUP三类定位冗余来源，补充行为探针校验测试未覆盖的行为改动，同时用相同标准评估开发者补丁作为基线。

## 关键结果
实验覆盖18个前沿模型的7660条GitHub Copilot CLI已解决轨迹，在SWE-bench Verified（6728条）和DeepSWE（932条）上验证：
1. SWE-bench上Agent补丁平均NPcode（代码单元必要精度）0.887，高于开发者基线的0.864，11/18模型的不必要代码量少于开发者，仅平均11%的代码单元为不必要。
2. 额外改动中61%为测试用例、13%为文档，仅21%为不必要代码；83%的不必要代码来自FIX步骤而非DEBUG调试残留。
3. 冗余清理：让Agent自审核每个改动的必要性精度65.7%、召回35.5%；结合Agent自生成测试+仓库回归测试剪枝，召回67.3%、精度46.3%，89%剪枝后补丁仍可正常解决任务。

## 核心结论
Agent任务成功率和生成内容质量没有强相关性，过度编辑问题需从评估指标新增必要精度、后处理分层剪枝、训练环节去冗余三方面共同优化。
