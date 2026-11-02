---
title: 'RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language
  Models'
title_zh: RangeSWA：面向连续扩散语言模型的免训练长度外推方法
authors:
- Guangfu Guo
- Xiaoqian Lu
- Linsey Pang
- Weiran Yao
- Haolin Chen
- Long Cheng
- Kunpeng Liu
affiliations:
- Clemson University
- University of Ottawa
- PayPal
- actAVA AI
arxiv_id: '2610.42084'
url: https://arxiv.org/abs/2610.42084
pdf_url: https://arxiv.org/pdf/2610.42084
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 扩散语言模型 · 免训练长上下文扩展
tags:
- LengthExtrapolation
- DiffusionLM
- AttentionMechanism
- TrainingFree
- LongContext
one_liner: 面向连续扩散语言模型的免训练长度外推方法，无需微调即可缓解长文本生成质量退化
practical_value: '- 做生成式推荐的长文案生成（如商品详情页、营销长文）时，可直接借鉴RangeSWA思路，无需微调扩散模型，仅通过改造注意力机制即可实现超训练长度的稳定生成，大幅节省微调成本

  - 扩散模型做长序列生成场景下，可复用「分阶段动态调整注意力窗口+条件注意力修正」的trick：高噪声阶段用大窗口抓全局语义，低噪声阶段用小窗口保局部细节，同时修正控制token的注意力权重避免比例失衡

  - 长序列生成评估不能只看PPL，需同时结合重复率、语义连贯性指标，避免低PPL但大量重复的无效生成，该评估思路可直接迁移到电商文案、营销内容的自动评估链路

  - 高并发线上生成场景可参考RangeSWA-Lite的裁剪思路，去掉远程摘要和检索模块，仅保留核心的条件修正和窗口调度，实现线性复杂度的长序列生成，兼顾效果和效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
连续扩散语言模型采用迭代降噪的双向上下文生成模式，相比自回归模型在可控生成上有独特优势，但生成长度超过训练长度时会出现严重的文本重复、语义漂移、质量退化问题。现有针对自回归模型的长度外推方法不适用这类双向迭代的扩散架构，且易出现低PPL掩盖高重复率的评估误区，限制了扩散语言模型在长文本生成场景的落地。
### 方法关键点
- 注意力机制融合本地滑动窗口、远程块摘要、动态内容检索三部分，在单个softmax内完成计算，既保留局部细节又支持长程上下文访问
- 引入位置重映射机制，将远距离交互的位置映射回训练范围内，解决位置失配问题；同时增加条件注意力修正，补偿长序列下控制token的注意力权重失衡
- 降噪阶段自适应窗口调度：高噪声阶段用1023窗口抓取全局语义，低噪声阶段用256窗口保障局部细节，最终解码阶段用2047窗口提升生成质量
- 提供轻量化版本RangeSWA-Lite，裁剪远程摘要和检索模块，仅保留核心修正逻辑，实现线性复杂度的推理
### 关键结果
在ELF-B/M/L、CoLa、LangFlow多个连续扩散模型上完成1k~8k长度外推实验，对比Full Attention、PI、NTK、Self-Extend、SWA等基线：
- ELF-M 8k场景下，相比SWA，RangeSWA将四元组重复率从7.7%降至1.2%，生成PPL从165.9降至32.1
- 8k长度下，RangeSWA相比Full Attention推理速度提升1.21倍，Lite版本提升1.62倍
- 消融实验显示条件注意力修正和自适应窗口调度贡献了主要的PPL下降，远程上下文访问进一步降低了重复率
### 核心结论
长序列生成的质量不能仅用PPL评估，低PPL往往会掩盖严重的文本重复问题，需结合重复率、语义连贯性等多指标综合判断
