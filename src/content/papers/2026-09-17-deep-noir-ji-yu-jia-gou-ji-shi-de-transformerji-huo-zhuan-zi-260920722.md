---
title: 'Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in
  Transformer Models'
title_zh: Deep Noir：基于架构计时的Transformer激活转向自动发现框架
authors:
- Frank E. Bobe
- Gregory D. Vetaw
- Darshan W. Bryner
- Matthew G. Cook
- Jose L. Salas-Vernis
affiliations:
- Naval Surface Warfare Center Panama City Division
- Office of Naval Research (ONR)
arxiv_id: '2609.20722'
url: https://arxiv.org/abs/2609.20722
pdf_url: https://arxiv.org/pdf/2609.20722
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM激活转向自动发现与安全评估
tags:
- Activation Steering
- Logit Lens
- Mechanistic Interpretability
- Prompt Injection
- LLM Safety
one_liner: 结合Logit Lens与头级因果归因自动发现最优激活转向参数，跨任务跨架构无需人工调参
practical_value: '- 做电商/广告场景的LLM分类任务（如垃圾评论识别、用户情感分类）时，可直接复用Deep Noir的5阶段参数搜索流程，仅需50个左右标注样本即可获得训练-free的激活转向配置，1B模型平均提16.7个点，7-9B模型最高提42.4个点，效果显著优于RepE等基线

  - 部署带激活转向的Agent（如电商客服Agent、广告投放决策Agent）时，可参考论文的转向强度-注入风险帕累托曲线选择最优参数，平衡任务效果与prompt注入风险，Gemma等架构可通过监控转向层激活norm实现注入检测

  - 若需将激活转向能力落地为无需runtime hook的生产版本，可参考论文的LoRA转换方案，注意现有转换存在约10%的精度损失，可优化蒸馏策略缩小gap

  - 做LLM干预优化时，避免直接修改权重，LayerNorm会将weight-space扰动衰减3-4个数量级，优先选择激活空间hook的干预方式'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有激活转向方法依赖人工选择干预层、注意力头子集与干预强度，跨架构跨任务迁移性差，且缺乏因果可解释性，无法量化评估转向带来的安全风险，无法满足Agent、生产级LLM应用对可控性、安全性的要求。
### 方法关键点
- 提出Architectural Chronometry核心思路，通过Logit Lens跟踪每层token概率从不确定到收敛的过程，结合注意力头级因果归因，自动筛选最优干预层与有效注意力头
- 5阶段无人工干预搜索流程：层排序→头隔离→方向计算→强度校准→最优参数选择，支持递归多层修正，自动回滚有损的干预配置
- 绕过weight-space修正的LayerNorm衰减问题，直接在激活空间注入扰动，干预效果可控
### 关键结果
- 测试覆盖3个参数规模（1B、2-3B、7-9B）共9款Transformer模型，任务包含垃圾邮件分类、SST-2情感分类、MMLU能力保留测试、prompt注入攻击测试，基线对比含RepE、CAA、随机搜索、少样本prompting
- 1B模型垃圾分类平均提升16.7个点，7-9B模型提升21-42.4个点；情感分类零代码迁移平均提升13.1个点，RepE在该任务上完全无提升
- 激活转向的prompt注入风险随干预强度单调上升，7B以上大模型转向反而能降低注入风险36.4个点
### 核心结论
基于机制可解释性的激活转向自动搜索比人工启发式方法的跨任务迁移性、鲁棒性显著更高，落地时必须同时兼顾效果、可解释性与安全边界
