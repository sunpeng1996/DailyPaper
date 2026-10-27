---
title: Hierarchical Skill Evolution for Coding Agent
title_zh: 面向代码Agent的分层技能演化框架HSE
authors:
- Jun Gao
- Yun Peng
- Changhai Zhou
- Yuhan Zhu
- Xiangyu Zeng
- Shiyang Zhang Yuhua Zhou
- Luozheng Qin
- Qian Qiao
- Xiaoteng Ma
- Baian Chen Weiyi Shang
arxiv_id: '2610.35616'
url: https://arxiv.org/abs/2610.35616
pdf_url: https://arxiv.org/pdf/2610.35616
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent技能自动化演化与迁移
tags:
- Agent
- Skill Evolution
- Code Agent
- Knowledge Distillation
- Transfer Learning
one_liner: 提出分层聚合轨迹知识的HSE框架，无需微调底层模型即可跨场景提升代码Agent性能
practical_value: '- 分层知识蒸馏思路可直接复用至推荐/电商Agent场景：将用户行为/业务决策轨迹按「单任务→同业务域→跨业务域」分层聚合，无需微调底层LLM即可蒸馏通用操作SOP与避坑规则，降低推理成本

  - Writer-Evaluator外置闭环可迁移到业务技能库自动迭代：无需人工标注技能，仅基于历史轨迹的成败反馈即可自动生成、筛选、更新技能库，大幅降低技能库的人工运营成本

  - 同步提炼正向成功技能与负向恢复技能的设计可复用：在客服Agent、营销决策Agent等易出错场景中，失败恢复技能对难例的性能提升贡献远超正向技能，可重点优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有代码Agent的技能复用方案存在明显缺陷：直接检索原始轨迹易过拟合特定任务/仓库的专属细节，泛化性差；通用领域知识又缺乏可落地的操作指导，无法有效指导复杂场景决策，且大多需要微调底层模型，落地成本高。
### 方法关键点
- 三层分层证据聚合：L1从单条执行轨迹提取带成败标签的任务级证据；L2同仓库内聚合高频模式生成仓库级候选技能；L3跨仓库聚合一致规律，分别提炼通用成功procedural技能与失败恢复技能
- 外置Writer-Evaluator闭环：底层代码模型完全冻结，仅迭代技能生成规则（Writer）与评估权重（Evaluator），自动过滤任务/仓库专属细节，保障技能泛化性
- 零标注目标场景适配：预训练好的Writer-Evaluator可直接迁移到新场景，仅基于新场景的轨迹数据与学习到的评估器即可更新专属技能库，无需新场景的标注反馈
### 关键实验结果
在SWE-bench Verified、DeepSWE两个代码基准上测试，覆盖GLM-5.2、GPT-5.5、Opus 4.8三类模型及两套Agent框架：
- 仅用SWE-Gym演化的10个通用技能，跨基准/模型/框架的前提下，较无技能基线提升1.9~7.7个百分点的任务解决率，优于所有对比基线
- 目标场景适配后，SWE-bench Verified上解决率最高达93.9%，DeepSWE最高达75.8%，较初始通用技能分别提升13.3、23.3个百分点
- 消融实验显示：去掉恢复技能在难例集DeepSWE上的性能损失可达5.6个百分点，去掉分层聚合逻辑最多损失3.8个百分点
### 核心结论
技能蒸馏的聚合粒度直接决定泛化性，同时覆盖成功经验与失败模式的技能库对复杂难场景的提升效果远好于仅保留正向经验的方案
