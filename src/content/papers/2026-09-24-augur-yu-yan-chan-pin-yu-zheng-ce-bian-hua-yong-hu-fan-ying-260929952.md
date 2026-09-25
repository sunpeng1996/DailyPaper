---
title: 'Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy
  Changes'
title_zh: Augur：预演产品与政策变化用户反应的合成决策实验室
authors:
- Rahul Khedar
- Mayank Malhotra
- Avinash Karn
affiliations:
- PayPal AI
arxiv_id: '2609.29952'
url: https://arxiv.org/abs/2609.29952
pdf_url: https://arxiv.org/pdf/2609.29952
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 用户反应模拟与决策评估
tags:
- Agent Simulation
- LLM Evaluation
- Prompt Engineering
- LoRA
- Synthetic Persona
one_liner: 提出预演产品政策变化用户反应的决策系统，证实大模型评估差异多来自prompt而非能力
practical_value: '- 做结构化决策类业务（如营销活动上线评估、定价调整预演）时，必须在prompt中明确定义输出分类的taxonomy，实测可提升所有大模型24~34pp准确率，避免无效评估

  - 用LoRA微调开源大模型落地业务决策任务时，无需盲目追云端SOTA，优化prompt后Qwen3-32B LoRA-SFT与GPT-5.2、Claude等无显著性能差异，部署成本更低

  - 搭建多Agent模拟用户反应链路时，不要盲目堆叠环节：仅在基础模型决策能力较弱时加模拟信号可提升20pp准确率，模型能力接近上限时模拟信号反而冗余，还会放大过度悲观偏差

  - 大模型业务效果评估不要只看与蒸馏教师的对齐度：实测教师对齐度从10%升至70%时，业务准确率几乎无变化，要优先用真实业务标注的基准集做评估'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

#### 动机
企业上线产品调整、政策修订、定价变更前，无法提前获知受众真实反应，上线后翻车风险高；现有大模型评估普遍存在偏差，无法准确区分云端SOTA与本地微调开源模型的真实能力差距，亟需可靠的预演系统与公平评估方法。

#### 方法关键点
- 构建Augur五阶段Pipeline：从变更文档抽取知识图谱 → 生成场景绑定的grounded persona群 → 基于OASIS引擎多轮模拟用户互动 → 检索证据生成决策报告，输出5类决策建议（ship/revise/delay/segment/mitigate）
- 构建Gold-50基准集：50个有公开真实结果的产品/政策变更案例，5类决策每类均衡10个，标注均经公开来源核验
- 做严格控制变量实验：固定模型权重、案例、打分逻辑，仅调整prompt是否包含分类定义模块，对比开源模型与云端SOTA的性能差异

#### 关键结果
- 仅调整prompt，同一Qwen3-32B LoRA-SFT准确率可从0%波动至73%；prompt加入分类定义后，所有云端SOTA准确率提升24~34pp，此时开源微调模型与云端SOTA无统计显著差异
- 合成用户反应可覆盖67~90%的真实公众顾虑；仅在基础模型仅靠标题决策准确率较低时，加入模拟信号可提升20pp，模型能力接近上限时模拟信号完全冗余
- 全Pipeline多阶段堆叠会放大过度悲观偏差，准确率反而低于仅报告阶段结果，甚至低于20%的五分类随机正确率

最值得记住的一句话：结构化决策任务的大模型评估必须同步公开prompt设计与输出合规率，否则排行榜衡量的不是模型判断力，而是prompt适配能力。
