---
title: Consilience for Verifier-Free Test-Time Scaling
title_zh: 面向无验证器测试时缩放的Consilience推理选择框架
authors:
- Lecheng Kong
- Like Hui
- Haitao Mao
- Jun Huan
affiliations:
- AWS AI Labs
arxiv_id: '2608.09898'
url: https://arxiv.org/abs/2608.09898
pdf_url: https://arxiv.org/pdf/2608.09898
published: '2026-08-10'
collected: '2026-08-11'
category: Reasoning
direction: LLM推理优化 · 无验证器测试时缩放
tags:
- Test-Time Scaling
- LLM Reasoning
- Confidence Calibration
- Verifier-Free
- Best-of-N
one_liner: 提出基于置信度时序不对称性的Consilience指标，解决复杂任务中置信度最大化选到自信错误结果的问题
practical_value: '- 电商商品文案生成、导购Agent多轮决策、生成式推荐理由生成等无外部验证器的场景，可直接用Consilience指标替代传统平均置信度做Best-of-N选优，避免「自信错误」的低质输出，难样本收益尤其显著

  - 工程实现零训练成本，仅需LLM返回token级top-K logprob（多数商用/开源模型均支持），超参数可默认固定为α=3、前后20%窗口、跳过前5%token，跨任务迁移性强无需逐任务调优

  - 对于带<think>推理分隔符的新模型，可先隔离推理段再计算得分，进一步提升选优效果；无分隔符模型可通过prompt添加「Final Answer」标记拆分，适配性极强

  - 算力敏感场景可按需触发：仅在搜索query理解、Agent工具调用等置信度低的难步骤启动多采样选优，平衡效果与成本，比如SWE-bench场景仅在代码编辑步骤启用仅增加125%时延'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有无验证器测试时缩放（VF-TTS）依赖全局置信度最大化做Best-of-N选优，在复杂推理任务上严重失效：难样本中错误答案的平均置信度反而高于正确答案，导致系统频繁选到「自信错误」的结果。而多数业务场景（如自由文案生成、Agent决策）没有外部验证器，非结构化输出也无法用多数投票选优，急需更鲁棒的无监督选优指标。
### 方法关键点
- 核心洞察：正确的复杂推理轨迹呈现「初始低置信→最终高置信」的时序不对称性：初始低置信代表模型在探索多种可行路径，全局高置信往往是过早收敛到错误路径的表现。
- 设计Consilience得分：`S = 最终W个token平均置信度 - α × 初始W个token平均置信度`，显式惩罚初始高置信、奖励最终收敛，默认W取序列长度的20%，跳过前5%与prompt关联的无差别token避免噪声。
- 推理阶段隔离：对于带<think>等推理分隔符的模型，仅在推理段计算置信度，剔除最终答案总结部分的人为高置信噪声，进一步提升指标区分度。
### 关键结果
在多个开源LLM上测试：
1. 自由代码生成LiveCodeBench：Consilience将GPT-OSS-120B准确率从Pass@1的65.7%提升到69.7%，难样本上AUROC达0.61~0.62，而平均置信度基线仅为随机水平0.47~0.50。
2. Agent任务SWE-bench：集成Consilience后，GPT-OSS-120B问题解决率从23.0%提升到26.9%，Qwen3-Coder从65.3%提升到67.3%，仅在编辑步骤启用仅增加125%时延。
3. 数学推理HMMT、研究生知识QA GPQA等任务上，Consilience均稳定优于Pass@1和所有置信度基线，超参数默认值可跨任务迁移。
> 最值得记住的一句话：复杂任务下不要一味追求全局高置信，初始的低置信代表有效探索，最终的收敛才是正确性的核心信号
