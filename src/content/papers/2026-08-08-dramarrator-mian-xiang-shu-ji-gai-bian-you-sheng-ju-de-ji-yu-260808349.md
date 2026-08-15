---
title: 'Dramarrator: Object-Based Audio Editing for Audio Drama Production from Books'
title_zh: Dramarrator：面向书籍改编有声剧的基于对象的音频编辑工具
authors:
- Karim Benharrak
- Oriol Nieto
- Bryan Wang
- Zeyu Jin
- Amy Pavel
affiliations:
- University of California, Berkeley
- Adobe Research
arxiv_id: '2608.08349'
url: https://arxiv.org/abs/2608.08349
pdf_url: https://arxiv.org/pdf/2608.08349
published: '2026-08-08'
collected: '2026-08-15'
category: Other
direction: 有声剧自动化创作 · 基于对象的编辑
tags:
- Audio Generation
- Content Creation
- Object-based Editing
- Multimodal Processing
- User Study
one_liner: 提出基于故事对象的有声剧创作工具，支持修改自动同步全链路资产，大幅降低制作门槛
practical_value: '- 可复用对象化素材管理思路，将广告/商品音频素材绑定到商品、品牌、场景对象，修改时自动同步全渠道物料，减少重复劳动

  - 多模态内容转制流程可参考其从文本自动提取结构化对象、生成对应多轨道音视频资产的管线，优化短视频/有声广告自动化生产效率

  - 内容生产工具设计可参考其对象级编辑+修改自动传播的交互逻辑，降低非专业运营的内容制作门槛'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有书籍改编有声剧流程高度依赖人工，角色、场景等故事元素跨多个关联资产存在，单点修改需全链路手动更新，制作成本极高。
### 方法关键点
1. 采用基于对象的音频编辑范式，将角色、场景等故事元素抽象为可编辑的独立对象
2. 自动从书籍文本提取故事对象，关联生成对应语音、音效、配乐三类音频资产，自动组装为多轨有声剧
3. 任意对象修改（如更换角色音色）自动同步到所有关联资产，无需手动逐一调整
### 关键结果数字
- 8名专业用户测试显示任务负载显著降低
- 300名听众测试表明经创作者微调的输出质量接近现有专业工具制作的成品
- 3人探索性测试显示该范式降低创作入门门槛，可泛化到有声剧外的音频制作场景
