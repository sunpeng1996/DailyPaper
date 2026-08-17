---
title: 'Seeing Red, Thinking Bad: Color Bias in Vision Language Models'
title_zh: 视觉语言模型的颜色偏差：视觉样式对文本语义解读的影响
authors:
- Kohsuke Ide
- Ryousuke Yamada
- Yoshihiro Fukuhara
- Hirokatsu Kataoka
- Yutaka Satoh
affiliations:
- National Institute of Advanced Industrial Science and Technology (AIST)
- University of Tsukuba
- University of Technology Nuremberg
- University of Oxford
arxiv_id: '2608.14286'
url: https://arxiv.org/abs/2608.14286
pdf_url: https://arxiv.org/pdf/2608.14286
published: '2026-08-14'
collected: '2026-08-17'
category: Multimodal
direction: 多模态大模型 · VLM偏差分析
tags:
- VLM
- Bias Analysis
- Visual Prompt
- Multimodal
- Robustness
one_liner: 提出Stealth Visual Prompts方法，揭示文本颜色、对比度等视觉样式会显著干扰VLM语义判断
practical_value: '- 电商广告/商品图文审核、多模态推荐场景中，需规避文本配色、对比度带来的VLM判断偏差，比如避免好评标绿、差评标红导致VLM情感分类错误

  - 研发基于VLM的多模态Agent时，输入的图文混合内容需设置文本与背景的对比度阈值，避免低对比度下VLM依赖视觉特征输出错误结果

  - 可复用Stealth Visual Prompts构造方法，对自研多模态模型做鲁棒性对抗测试，提前定位视觉样式类偏差，优化模型泛化性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
VLMs已广泛落地于推荐、招聘等工业决策系统，但文本的视觉样式对其语义理解的干扰尚未被系统分析，黑盒VLM的隐含偏差难以定位。
### 方法关键点
提出Stealth Visual Prompts范式，在完全保留文本语义的前提下，仅调整颜色、对比度等视觉属性，批量生成测试样本，同时追踪视觉编码器隐层表征的变化。
### 关键结果
- 正向词汇标注为绿色时，会持续拉偏VLM的情感预测结果向正向，甚至完全忽略文本中存在的负面内容
- 文本与背景对比度降低时，VLM会更依赖视觉显著性特征，VQA任务错误率显著提升
- 上述偏差与颜色变化导致的视觉编码器隐层表征偏移直接相关
