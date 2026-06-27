---
title: 'RoPEMover: Depth-Aware Object Relocation via Positional Embeddings'
title_zh: RoPEMover：基于位置嵌入的深度感知对象重定位方法
authors:
- Ipek Oztas
- Duygu Ceylan
- Aybars Bugra Aksoy
- Aysegul Dundar
affiliations:
- Bilkent University
- Brown University
- Adobe Research
arxiv_id: '2606.27332'
url: https://arxiv.org/abs/2606.27332
pdf_url: https://arxiv.org/pdf/2606.27332
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 图像编辑 · 深度感知RoPE优化
tags:
- RoPE
- Diffusion Transformer
- Image Editing
- 3D Spatial Encoding
- PEFT
one_liner: 扩展RoPE为深度感知版本，实现单张图像几何一致的对象重定位与场景编辑
practical_value: '- 电商商品图修图场景可复用深度感知RoPE思路，调整商品位置/前后景时自动匹配光影、遮挡，降低美工工作量

  - 多模态生成类推荐（如穿搭效果图、家居摆放图生成）可借鉴RoPE显式操控空间位置的方法，提升生成图几何一致性

  - 低资源场景可复用「大量合成数据+少量真实数据PEFT」策略，降低场景定制的标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单图内对象移动需满足遮挡处理、新暴露区域补全、光影反射一致等几何一致性要求，现有方法难以维持场景级一致性，效果不佳。
### 方法关键点
1. 利用RoPE的结构化空间场特性，直接操控扩散Transformer的位置表征实现可控对象移动；
2. 将2D RoPE扩展为深度感知版本，编码3D空间结构，支持对象前后景摆放、位移时的场景感知更新；
3. 采用合成数据加少量真实图像的PEFT策略训练，降低标注依赖。
### 关键结果
在标准对象移动基准所有评估指标上达到SOTA，大空间位移下仍保留对象身份，新暴露区域生成合理，可自动同步更新阴影、光照等场景效果，还支持对象移除、新增等下游编辑任务。
