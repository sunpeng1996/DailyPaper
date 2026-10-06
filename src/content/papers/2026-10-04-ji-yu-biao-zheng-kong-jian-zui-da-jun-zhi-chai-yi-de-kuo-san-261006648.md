---
title: Representation-Space MMD for Diffusion Language Models
title_zh: 基于表征空间最大均值差异的扩散语言模型后训练方法
authors:
- Ilya Drobyshevskiy
- Ilia Sudakov
- Maksim Semenov
- Denis Kuznedelev
- Maksim Ignatov
- Pavel Temirchev
- Nikita Balagansky
- Viacheslav Meshchaninov
- Nikita Gushchin
- Dmitry Baranchuk
affiliations:
- Yandex Research
- HSE University
- Applied AI Institute
- T-Tech
- Constructor University
arxiv_id: '2610.06648'
url: https://arxiv.org/abs/2610.06648
pdf_url: https://arxiv.org/pdf/2610.06648
published: '2026-10-04'
collected: '2026-10-06'
category: Training
direction: 扩散语言模型 · 后训练优化
tags:
- Diffusion Language Model
- MMD
- Post-training
- Sampling Efficiency
- Text Generation
one_liner: 通过冻结扩散语言模型表征空间MMD后训练，无需教师/辅助模型即可提升少步生成效率与质量
practical_value: '- 生成式推荐/Agent的文本生成模块若采用扩散语言模型，可直接复用该后训练方法，无需额外教师模型，仅用冻结自身表征的MMD损失即可提升少步采样质量、降低推理时延

  - 做生成任务分布对齐时，可借鉴token级RBF核MMD设计，保留每个位置的上下文特征计算分布差异，效果优于序列池化或仅匹配均值，且无需额外训练判别器

  - 扩散模型做并行解码时，可参考16B大模型优化经验，仅需几百步训练即可提升10%+的解码并行度，同时保持生成精度，适配业务侧高吞吐推理需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有扩散语言模型（DLM）的少步采样优化方法大多依赖教师模型蒸馏或联合训练的辅助模型，训练成本高、流程复杂，亟需无需额外辅助模块的高效后训练方案，平衡生成质量与推理速度。

### 方法关键点
- 特征提取：用冻结的预训练DLM提取生成样本与参考样本的token级上下文特征，单序列可获得多组观测，提升MMD估计效率
- 离散DLM优化：对采样序列用带留一基线的REINFORCE策略梯度优化MMD奖励，适配masked、混合mask-均匀等多种离散扩散架构
- 连续DLM优化：梯度直接通过生成隐态回传，训练单步隐态生成器后支持自条件迭代优化，还可搭配迭代精炼蒸馏进一步降低采样步数
- 损失设计：采用token级RBF核计算MMD，同时保留生成样本内的排斥项，避免生成坍缩

### 关键实验
数据集覆盖OpenWebText（无条件生成）、GSM8K/TinyGSM（数学推理）、16B DMax模型（数学/代码生成），对比IDLM、DiDi-Instruct、ELF、ELF-PD等主流少步DLM方案。核心结果包括：OpenWebText上匹配熵时生成困惑度比IDLM低17~21%；GSM8K上4步采样准确率比ELF-PD高4.9个百分点；16B DMax模型后训练仅需1.7~2.5 GPU小时，解码并行度提升10.3~16.5%，代码基准准确率最高提升3.8个百分点。

利用模型自身冻结表征的分布匹配损失，即可低成本实现扩散语言模型的采样效率与质量双提升，无需引入额外复杂辅助模块。
