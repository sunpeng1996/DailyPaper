---
title: 'Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in
  Image-Conditioned VLMs via Dual-Prompted LoRA Decoders'
title_zh: 基于双提示LoRA解码器的图像条件VLM字符级幻觉跨度检测
authors:
- Mikhail Kulakov
- Ruslan Solikhov
- Ivan Bondarenko
affiliations:
- Novosibirsk State University
arxiv_id: '2611.14100'
url: https://arxiv.org/abs/2611.14100
pdf_url: https://arxiv.org/pdf/2611.14100
published: '2026-11-10'
collected: '2026-11-11'
category: Multimodal
direction: 多模态大模型 · 幻觉检测
tags:
- LoRA
- VLM
- Hallucination Detection
- Multimodal
- Character-level Detection
one_liner: 基于冻结Gemma+双提示LoRA实现多语言VLM字符级幻觉检测，性能超官方基线2倍
practical_value: '- 电商多模态商品文案生成、导购VQA Agent的幻觉校验场景，可复用同基座+LoRA的轻量校验方案，无需独立部署校验模型，大幅降低推理成本

  - 针对因果解码器无法获取双向上下文的痛点，可采用prompt内重复待检测文本、取第二次出现位置表征的trick，低成本实现近似双向注意力效果

  - 多语言多模态内容合规校验场景，可复用字符级BIO边界预测+分语言分类器的架构，精准定位幻觉片段并识别错误类型'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
图像条件VLM的幻觉问题是多模态系统可靠性核心瓶颈，现有方法难以精准定位多语言场景下的字符级幻觉片段，且独立校验模型部署成本高。
### 方法关键点
1. 采用冻结Gemma-4-12B-it作为基座，仅训练约10.7M参数的LoRA适配器，大幅降低训练与部署成本
2. 提出双提示方案：在单条prompt内重复待检测回答，从第二次出现的位置提取表征，为因果解码器提供近似双向上下文
3. 字符级定位器融合中间隐层输出预测幻觉概率、BIO边界与全局弃权分数，搭配分语言分类器识别5类幻觉类型
### 关键结果
闭测集宏观平均字符IoU达0.4404，是官方基线0.1854的2倍以上，英/法/意/中4种语言IoU排名5-6位；消融实验显示重复回答带来的收益与LoRA适配相当，打乱图文配对后IoU降至随机预测水平
