---
title: 'DiSCO: Defending text-to-image generation through distribution-guided contrastive
  prompt optimization'
title_zh: DiSCO：基于分布引导对比Prompt优化的文生图生成防御方法
authors:
- Tong Zhang
- Motasem Alfarra
- Carlos Hinojosa
- Christos Louizos
- Bernard Ghanem
affiliations:
- King Abdullah University of Science and Technology (KAUST)
- Qualcomm AI Research
arxiv_id: '2608.17067'
url: https://arxiv.org/abs/2608.17067
pdf_url: https://arxiv.org/pdf/2608.17067
published: '2026-08-16'
collected: '2026-08-19'
category: Other
direction: 文生图安全 · 黑盒Prompt优化
tags:
- PromptOptimization
- TextToImageSafety
- BlackBoxDefense
- ContrastiveLearning
- ZeroShot
one_liner: 提出零样本纯黑盒Prompt级文生图安全防御方案，无需改模型即可降低有害内容生成率
practical_value: '- 做电商AI作图、Agent生成内容等生成类业务安全管控时，可复用该纯黑盒Prompt优化思路，无需改动底层模型即可适配闭源商用生成API的安全需求

  - 针对「语义合法但触发生成有害内容」的漏判场景，可参考基于目标模型生成的正负样本池做对比打分的Prompt校正逻辑

  - 对需要零样本适配、不能侵入模型的安全管控场景，可复用Beam搜索加迭代自适应反馈的Prompt优化工程范式'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
文生图模型商业化落地过程中，NSFW等有害内容生成风险突出，现有白盒防御方案依赖模型权重访问/修改，无法适配闭源专有模型；现有黑盒Prompt改写方案无法解决「语言层面安全但因模型训练分布触发有害生成」的良性对抗漏判问题。

### 方法关键点
提出零样本纯黑盒插件式防御模块DiSCO，完全在Prompt层工作，无需模型重训、微调或访问内部权重；通过Beam搜索做分布引导的Prompt后缀扩展，基于目标模型自身生成的安全/非安全图像池做对比打分优化，迭代自适应反馈直到生成安全内容。

### 关键结果数字
在I2P基准多红队攻击场景下，对无防御/已有防御模型分别降低37.7%、25.13%的攻击成功率（ASR）；全32种系统-攻击配置下平均ASR从23.6%降至2.4%（NudeNet检测）、8.3%降至1.7%（Q16检测），同时保留语义保真度、提升图像一致性。
