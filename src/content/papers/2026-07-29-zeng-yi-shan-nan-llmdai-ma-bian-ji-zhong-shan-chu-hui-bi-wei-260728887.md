---
title: 'To Add Is Machine, To Delete Is Human: Measuring and Mitigating Deletion Avoidance
  in LLM Code Editing'
title_zh: 《增易删难：LLM代码编辑中删除回避行为的度量与缓解》
authors:
- Amir M. Ebrahimi
- Mohammed Mehedi Hasan
- Aaditya Bhatia
- Gopi Krishnan Rajbahadur
- Ahmed E. Hassan
affiliations:
- Queen's University
arxiv_id: '2607.28887'
url: https://arxiv.org/abs/2607.28887
pdf_url: https://arxiv.org/pdf/2607.28887
published: '2026-07-29'
collected: '2026-08-06'
category: LLM
direction: LLM代码编辑行为优化
tags:
- LLM
- Code Editing
- Benchmark
- Post-training
- Evaluation
one_liner: 发现LLM代码编辑的删除回避问题，构建专属评测基准，验证后训练注入删除逻辑的优化效果
practical_value: '- 开发编码类Agent（如推荐系统特征工程、策略迭代自动化Agent）时，可针对性加入删除操作校验逻辑，避免冗余代码拉高生产维护成本

  - 自研代码领域垂域LLM时，可在SFT/后训练阶段补充代码删除场景样本，降低删除回避问题，提升生成代码的可落地性

  - 对Agent生成的可运行代码做上线前校验时，可增加冗余代码检查环节，拦截Guard-and-Go类无效修复流入生产'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM生成的可通过测试的代码补丁往往维护性差，核心成因未得到明确拆解，编码Agent的输出落地性不足。
### 方法关键点
1. 定义「删除回避」现象：LLM系统性保留应删除代码的行为，识别Guard-and-Go冗余补丁模式；
2. 构建CanItDelete基准，包含200个从真实提交挖掘的纯删除需求任务；
3. 消融不同prompt策略，验证后训练阶段注入删除任务的优化效果。
### 关键结果数字
SWE-bench榜单Top5模型删除召回最高仅71.7%，即便定位到正确文件，准确删除目标行的概率低于52%；29%的过测补丁采用Guard-and-Go冗余逻辑；新增删除校验测试后，前沿模型通过率从63.2%降至41.9%；纯删除任务下最优模型仍有20%失败率，后训练优化可有效降低删除回避问题。
