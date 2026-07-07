---
title: Noisy-Channel Minimum Bayes Risk Decoding
title_zh: 基于噪声信道的最小贝叶斯风险解码方法
authors:
- Yusuke Sakai
- Hidetaka Kamigaito
- Taro Watanabe
affiliations:
- Nara Institute of Science and Technology, Japan
arxiv_id: '2607.05198'
url: https://arxiv.org/abs/2607.05198
pdf_url: https://arxiv.org/pdf/2607.05198
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: 大语言模型解码优化 · MBR解码
tags:
- MBR Decoding
- Noisy Channel
- Text Generation
- LLM Inference
- Utility Metric
one_liner: 将MBR解码分解为四个可加权概率组件，解决其与非对称评价指标的适配偏差
practical_value: '- 生成式推荐/Agent回复的候选重排场景，可复用四组件加权框架，结合业务评价指标（如点击率、语义匹配度）调整各通道权重，提升生成质量

  - 若使用BERTScore类对称语义指标作为业务对齐目标，可适当调高假设到参考似然（α）和参考先验（δ）权重，无需额外调整就能跨任务稳定收益

  - 若使用BLEU/ChrF类表面匹配指标，可保留较高的假设先验（β）权重，降低参考到假设似然（γ）权重，规避重复、语义偏离问题

  - 该方法仅需在现有MBR重排逻辑上新增简单加权运算，额外开销可忽略，可直接接入现有生成式推荐/Agent的后处理链路'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统MBR解码通过优化伪参考下的期望效用提升生成质量，效果优于MAP解码，但存在设计偏差：BLEU、COMET等主流评价指标均为非对称，原有MBR仅考虑参考到假设的单向匹配关系，未纳入双向交互、假设/参考先验的影响，无法充分对齐评价目标，限制生成效果进一步提升。
### 方法关键点
- 基于噪声信道对MBR解码做概率分解，得到四个独立可控组件：假设到参考似然P(r|h)、参考到假设似然P(h|r)、假设先验P(h)、参考先验P(r)
- 为每个组件引入可调权重α、β、γ、δ，通过权重调整适配不同评价指标的特性，可统一复现现有所有MBR变种的计算逻辑
- 仅需在现有MBR的候选打分阶段增加简单加权运算，额外计算开销可忽略，工程落地成本极低
### 关键结果
在12个机器翻译场景、3个文本摘要数据集、2个图像字幕数据集上验证，对比原始MBR解码：使用BERTScore作为效用函数时，最优权重配置可稳定带来1-2个z-score的性能提升；跨任务/数据集迁移最优权重时，WMT22 En-De的最优配置迁移到WMT23 En-De，ChrF得分从50.05提升至50.18；通道权重的最优配置仅和选择的效用指标强相关，和任务类型几乎无关。
### 核心结论
MBR解码的效果瓶颈主要来自和效用指标的方向适配，而非任务特性，通过四通道加权调整即可在几乎无额外开销的情况下稳定提升生成质量。
