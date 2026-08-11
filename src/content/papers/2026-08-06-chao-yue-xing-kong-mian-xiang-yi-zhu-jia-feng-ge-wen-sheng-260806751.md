---
title: 'Beyond Starry Night: Shortcut-Aware Control-State Planning for Artist-Grounded
  Text to Image Generation'
title_zh: 超越星空：面向艺术家风格文生图的感知捷径控制态规划框架
authors:
- Kuan Xing
- Ye Wang
- Changyi Gan
- Yuheng Li
- Thao Nguyen
- Yi Chang
- Yilin Wang
affiliations:
- Jilin University
- Adobe
- University of Wisconsin
arxiv_id: '2608.06751'
url: https://arxiv.org/abs/2608.06751
pdf_url: https://arxiv.org/pdf/2608.06751
published: '2026-08-06'
collected: '2026-08-11'
category: Multimodal
direction: 多模态文生图 · 风格对齐与生成控制
tags:
- Text-to-Image
- Style Alignment
- Shortcut Mitigation
- Control Planning
- Evaluation Benchmark
one_liner: 提出感知生成捷径的Atelier框架，解决艺术家风格文生图的用户指定内容被篡改问题
practical_value: '- 电商AI设计、营销素材生成等定制化风格生成业务，可复用「显式拆分保留项/转换项/规避项」的控制态设计，避免风格捷径覆盖用户指定的商品/场景要素

  - 多模态Agent生成流程可参考「知识锚定控制态→生成后端适配计划→全局+局部反馈迭代调优」的pipeline，提升结果符合度

  - 风格类生成效果评估可复用ArtIntentBench的分层逻辑，覆盖风格保真、结构保留、捷径规避、用户偏好多个维度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有艺术家风格文生图存在明显捷径问题：模型仅依赖艺术家名称关联的高频motifs、通用调色板、时代特征生成，频繁篡改用户指定的场景内容，仅靠提示工程、RAG无法解决。

### 方法关键点
1. 提出Atelier框架，将模糊的艺术风格意图解析为显式控制态，拆分场景锚点、保留/转换规则、风格假设、艺术家证据、捷径规避约束；
2. 基于艺术家知识库+局部patch参考锚定控制态，生成适配后端模型的生成计划；
3. 通过全局+局部真实性反馈迭代优化生成结果。同时推出ArtIntentBench基准，覆盖梵高、齐白石2位艺术家的5类评估任务。

### 关键结果
对比提示工程、RAG、通用Agent基线，无论对接开源还是闭源生成器，Atelier的艺术家风格保真度、源结构保留率显著提升，捷径替换率大幅降低。
