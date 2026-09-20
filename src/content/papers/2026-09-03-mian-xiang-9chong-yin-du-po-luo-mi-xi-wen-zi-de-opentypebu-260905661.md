---
title: 'Srijika: OpenType-Layout-Reusing Font Restyling for Nine Indic Scripts'
title_zh: 面向9种印度婆罗米系文字的OpenType布局复用字体风格重生成系统
authors:
- Anil Pai
affiliations:
- Loopdesk Technologies LLP
arxiv_id: '2609.05661'
url: https://arxiv.org/abs/2609.05661
pdf_url: https://arxiv.org/pdf/2609.05661
published: '2026-09-03'
collected: '2026-09-20'
category: Other
direction: 多语言字体生成 · 布局复用风格迁移
tags:
- Font Generation
- Latent Diffusion
- Layout Reuse
- OpenType
- Indic Scripts
one_liner: 基于模板布局复用+参考条件扩散模型生成符合OpenType规范的多印度文字体
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
印度文字体需兼容数百上千种连写、半形、元音变体的OpenType shaping规则，从零生成的字体普遍存在布局兼容问题，开发成本极高。
### 方法关键点
1. 复用成熟模板字体的cmap、GSUB规则，在标准化度量策略下保留GPOS数据，生成字体天然符合OpenType规范
2. 基于覆盖650个开源字族的Lipika检索索引实现自然语言风格匹配，用参考条件潜扩散模型重绘字形，搭配校验回退机制保障可靠性
3. 新增单种文字仅需20-48k步训练，跨文字路由避免多语言训练的效果稀释问题
### 关键结果
生成66个TTF字体全部通过OpenType Sanitizer校验，覆盖80915个字形、54812个锚点的全闭包审计完成度量变化量化；留出训练字族的SSIM测试中，模板拷贝在50/56个字体上优于生成结果，仅1个OOD字族实现0.85-0.94的风格迁移效果。
