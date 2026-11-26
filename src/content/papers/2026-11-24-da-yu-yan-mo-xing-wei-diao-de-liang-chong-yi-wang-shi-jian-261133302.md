---
title: 'Two Timescales of Forgetting in Fine-tuning of Language Models: Fast Behavioral
  Suppression and Slow Representational Drift'
title_zh: 大语言模型微调的两种遗忘时间尺度：快速行为抑制与慢速表征漂移
authors:
- Yilin Luo
- Jin Hwa Lee
- Andrew M. Saxe
- Antonio Sclocchi
affiliations:
- Principia
- University College London
- Université Paris-Saclay
arxiv_id: '2611.33302'
url: https://arxiv.org/abs/2611.33302
pdf_url: https://arxiv.org/pdf/2611.33302
published: '2026-11-24'
collected: '2026-11-26'
category: Training
direction: LLM 微调遗忘机制研究
tags:
- SFT
- catastrophic_forgetting
- fine-tuning
- representation_learning
- alignment
one_liner: 发现LLM SFT存在行为快速抑制、表征慢速漂移两种遗忘时间尺度，揭示各自驱动机制
practical_value: '- 做电商/广告垂直领域SFT时，千步以内短微调即可快速压制通用领域无关输出，无需过长训练，既能降算力成本，还能保留预训练通用语义表征，避免冷启动泛化性下降

  - 若要彻底擦除预训练学到的敏感规则/违规内容，不能仅依赖输出行为评测，需补充表征探针检测；可通过调高weight decay加速对应表征漂移删除，若要保留跨域能力可添加L2正则锚定预训练参数

  - 跨场景迁移（比如从通用推荐话术模型微调为大促专属模型）后，短步数微调的模型仍保留原场景完整表征，可通过prompt工程、小样本微调快速唤醒原能力，无需全量重训'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前大语言模型预训练后SFT的遗忘机制认知存在明显缺口：行为层面的能力下降不代表对应内部表征已被删除，这对安全对齐、领域微调、选择性遗忘等场景的策略设计影响极大，急需明确行为遗忘与表征遗忘的动态差异与驱动逻辑。
### 方法关键点
- 采用可控的随机层次模型（RHM）语法生成数据预训练Decoder-only Transformer，再用删减部分生成规则的子集做SFT，可独立追踪删除规则的生成行为和内部表征变化
- 设计三类测试集（保留规则生成、删除规则生成、上下文含删除规则），搭配生成探针、表征探针分别量化行为遗忘和表征遗忘程度
- 补充双语自然语言、代码生成LLM微调实验，验证结论在真实场景的普适性
### 关键结果
- 行为遗忘速度比表征遗忘快2~3个数量级：RHM实验中删除规则的生成行为在100步内被完全压制，对应表征的漂移要到1e4~1e6步才发生
- 行为抑制速度与学习率成反比，由梯度的均值信号驱动；表征漂移速度与学习率平方成反比，由梯度更新的噪声累积驱动
- 向预训练参数添加L2正则可延缓甚至阻止表征遗忘，weight decay会加速表征漂移

最值得记住的结论：短步数SFT仅能压制不需要的行为输出，对应底层表征仍完整保留，可通过特殊prompt或小样本重新唤醒。
