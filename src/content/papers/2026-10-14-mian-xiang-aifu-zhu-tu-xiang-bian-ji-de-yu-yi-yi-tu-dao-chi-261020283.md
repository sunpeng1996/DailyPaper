---
title: From Semantic Editing Intentions to Persistent Parametric Controls for AI-Assisted
  Image Editing
title_zh: 面向AI辅助图像编辑的语义意图到持久参数控制转换方法
authors:
- Rifat Mehreen Amin
- Michelle Dutoit
- Anton Rockenstein
- Baptiste Caramiaux
- Andreas Butz
affiliations:
- LMU Munich
- CNRS
- Sorbonne Université
arxiv_id: '2610.20283'
url: https://arxiv.org/abs/2610.20283
pdf_url: https://arxiv.org/pdf/2610.20283
published: '2026-10-14'
collected: '2026-10-17'
category: Other
direction: AI辅助图像编辑 · 意图转参数控制
tags:
- ImageEditing
- Human-AIInteraction
- IntentUnderstanding
- UserStudy
- ParametricControl
one_liner: 提出Atelier语义图像编辑工具，将用户高层编辑意图转换为可手动调整的参数化控件
practical_value: '- 电商商品图AI修图场景可复用「高层意图转可调节参数控件」框架，避免AI生成结果不可控，支持运营微调修图效果

  - 可借鉴编辑控件与编辑对象绑定、同套编辑参数跨对象复用的设计，提升批量商品图修图效率

  - 产品设计上需额外增加AI参数生成逻辑的可解释性模块，降低用户对AI输出的不信任感'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AI图像编辑工具仅支持用户输入高层语义意图、AI直接输出最终编辑结果，中间转换逻辑黑盒、用户无法微调，难以满足专业编辑场景的可控性需求。
### 方法关键点
1. 基于8名图像编辑从业者的形成性研究，设计Atelier编辑工具，输入图像+用户编辑意图后，自动匹配输出上下文相关的可操纵参数控件，而非直接生成最终图；
2. 支持编辑范围（全图/对象/套索区域）选择、控件与编辑对象绑定、同套编辑参数跨对象复用等功能。
### 关键结果数字
12名从业者的被试内实验显示，用户普遍偏好AI生成的参数控件方案，认为其支持创意探索，且会主动微调AI给出的初始参数；但用户对AI生成特定控件及数值的原因感知度较低，可解释性仍有不足。
