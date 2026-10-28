---
title: 'ReGE: Stronger Agents through Experience Synthesis'
title_zh: ReGE：基于经验合成的增强智能体执行框架
authors:
- Jiarong Liang
- Yubo Wang
- Zijie Liu
- Yuxuan Zhang
- Ping Nie
- Wenhu Chen
affiliations:
- University of Waterloo
- University of North Carolina at Chapel Hill
- University of British Columbia
arxiv_id: '2610.33861'
url: https://arxiv.org/abs/2610.33861
pdf_url: https://arxiv.org/pdf/2610.33861
published: '2026-10-23'
collected: '2026-10-28'
category: Agent
direction: 智能体 · 执行经验合成复用
tags:
- Agent
- Experience_Synthesis
- Inference_Efficiency
- LLM
- Cost_Optimization
one_liner: 基于同一底座模型单轮合成多轮执行经验生成指导，无参数更新即可提升智能体任务成功率并降低成本
practical_value: '- 电商/广告域任务型Agent（如智能客服、商品信息查询Agent）可直接复用多轮执行的成功/失败轨迹，通过单轮Coach调用合成结构化可执行指导，无需模型微调即可提升同场景任务成功率，同时降低推理成本

  - 搜索推荐冷启动场景（如新Query意图理解、新商品类目匹配）可汇总多轮探测的中间结果，用ReGE-Syn联合合成执行指导，减少重复试错带来的token消耗

  - 大促等场景下的并行多智能体集群（如推荐策略验证Agent）的执行结果可通过ReGE统一聚合，仅用28%成本即可达到更高阶模型的任务效果，适合算力预算有限的降本场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有交互智能体重复执行同任务时会产生大量已验证事实、有效操作、失败经验，但全量复用历史轨迹会带来极高token成本，逐轨迹独立摘要又会丢失跨尝试的关联信息，如何低成本复用自身执行经验提升后续任务效果是核心痛点。

### 方法关键点
1. 全链路复用同一底座LLM，无需参数更新、无需更强教师模型，分经验池构建、联合合成、引导执行三个阶段
2. ReGE-Syn核心实现：单轮Coach调用即可将多轮尝试的轨迹、 artifacts、坑点联合合成自包含的可执行指导，无需对单条轨迹做预摘要
3. 学生智能体从初始环境状态出发，结合当前观测可验证、调整、跳过指导步骤，无需继承历史环境的中间状态

### 关键实验结果
在Terminal-Bench 2.0、Spider2-Lite、AndroidWorld、BrowseComp-Plus4个基准上测试，对比无引导执行、Reflexion、AggAgent等基线：
1. 平均提升GPT系列模型任务准确率9.9个百分点，Claude系列提升8.8个百分点
2. 对比AggAgent，ReGE-Syn在BrowseComp-Plus数据集上减少98.2%（GPT）/95.5%（Claude）的指导构建token，总token消耗（构建+执行）分别下降15.7%、35.4%
3. 低阶gpt-5.6-luna叠加ReGE后可达到高阶gpt-5.6-sol的任务成功率，仅需后者28%的推理成本

最值得记住的一句话：智能体不需要盲目升级更大的模型，仅通过低成本合成自身的多轮执行经验，就能用远低于高阶模型的成本达到同等任务效果
