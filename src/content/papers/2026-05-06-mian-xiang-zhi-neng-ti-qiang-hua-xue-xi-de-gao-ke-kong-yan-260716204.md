---
title: Masked Diffusion Language Models are Strong and Steerable Text-Based World
  Models for Agentic RL
title_zh: 面向智能体强化学习的高可控掩码扩散语言模型文本世界模拟器
authors:
- Darshan Deshpande
affiliations:
- Patronus AI
arxiv_id: '2607.16204'
url: https://arxiv.org/abs/2607.16204
pdf_url: https://arxiv.org/pdf/2607.16204
published: '2026-05-06'
collected: '2026-07-22'
category: Agent
direction: Agent强化训练 · 文本世界模型构建
tags:
- MDLM
- World Model
- Reinforcement Learning
- LLM Agent
- Structured Generation
one_liner: 掩码扩散语言模型构建文本世界模型，效果超4倍参数自回归LLM，RL智能体零-shot提分47%
practical_value: '- 电商客服/履约类Agent的环境模拟可替换自回归LLM为MDLM，双向锚定能力避免状态字段全局不一致（如退款成功与状态为error的矛盾），大幅降低结构化输出幻觉

  - 生成Agent训练合成轨迹时，MDLM生成样本Self-BLEU更低、多样性更高，可缓解训练模式坍塌，适合小样本场景扩充训练数据

  - 结构化输出场景（如API调用结果、订单状态更新）可直接用MDLM的锚定生成能力，无需额外约束即可保证指定字段符合schema要求，降低后处理成本

  - 8B参数MDLM效果超35B自回归LLM，推理延迟相当，适合低资源场景的Agent环境部署，可显著降本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RL智能体训练依赖手工构建的静态环境，Reward稀疏、分布偏移问题严重，自回归LLM做世界模型存在左到右因果偏差，无法适配全局依赖的状态锚点（如工具Schema、历史上下文、固定输出字段），容易生成全局不一致的结果，导致样本质量差、训练模式坍塌。

### 方法关键点
- 将文本世界建模拆解为初始环境状态、任务上下文、工具Schema、域规则、可控指令5个固定组件，建模状态转移的条件分布
- 利用MDLM的双向去噪能力，支持任意锚点字段固定的并行生成，彻底规避自回归模型的前缀偏差问题
- 构建239403条跨9个开源环境、12个前沿模型的状态-动作轨迹数据集，配套即插即用的GRPO训练框架，加入确定性状态校验逻辑

### 关键结果
- 8B参数SDAR（MDLM变种）在域内MAUVE达0.982，超过35B参数自回归LLM的0.932，参数量仅为后者1/4，推理延迟相当
- 零-shot迁移到3个分布外环境，用MDLM生成轨迹训练1.2B-7B的RL智能体，任务成功率较自回归世界模型基线最多提升47%
- 人类评估在真实度、结果正确性、训练效用上的平均分分别达4.75、4.25、4.5（1-5分制），标注一致性α≥0.89

**最值得记住的结论**：自回归的因果归纳偏差，而非参数量，才是当前LLM做文本世界模型的核心瓶颈。
