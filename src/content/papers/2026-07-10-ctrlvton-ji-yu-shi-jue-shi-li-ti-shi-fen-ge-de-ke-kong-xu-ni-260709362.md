---
title: 'CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation'
title_zh: CtrlVTON：基于视觉实例提示分割的可控虚拟试穿
authors:
- Seungyong Lee
- Hyun Jun Jang
- Sangoh Kim
- Sungjoon Park
affiliations:
- NXN Labs
- KAIST
arxiv_id: '2607.09362'
url: https://arxiv.org/abs/2607.09362
pdf_url: https://arxiv.org/pdf/2607.09362
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 多模态可控生成 · 电商虚拟试穿
tags:
- Virtual Try-On
- Controllable Generation
- Visual Prompt
- SAM
- Segmentation
- E-commerce
one_liner: 推出实例级分割模型VIP-SAM与支持细粒度穿戴控制的可控虚拟试穿框架CtrlVTON
practical_value: '- 电商服饰类虚拟试穿场景可直接复用CtrlVTON的掩码控制逻辑，支持用户自定义宽松度、塞衣角、开衫状态等穿戴效果，提升交互体验

  - 服饰实例分割任务可参考VIP-SAM的实例级提示方案，替代传统类别级分割，适配同品类不同款式服饰的精准识别需求

  - 可将该可控试穿能力接入商品导购Agent、直播带货场景，降低用户服饰购买决策成本，提升转化率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前虚拟试穿（VTO）仅能实现服饰向目标人物的迁移，缺乏穿戴尺寸（宽松/合身）、风格（塞衣角/敞开等）、身体摆放位置的细粒度控制能力，无法满足电商用户个性化试穿需求。

### 方法关键点
1. VIP-SAM解决视觉实例提示分割任务：输入服饰平铺图即可精准分割穿搭场景下的对应具体服饰，属于实例级任务，区别于传统类别级分割。
2. CtrlVTON可控虚拟试穿框架将试穿重构为图像编辑任务，通过分割掩码实现像素级服饰布局控制，支持自定义穿戴效果。

### 关键结果
两项任务均达到SOTA，CtrlVTON对用户指定布局的遵循度远超现有最强商业编辑系统，服饰还原度与商业系统持平。
