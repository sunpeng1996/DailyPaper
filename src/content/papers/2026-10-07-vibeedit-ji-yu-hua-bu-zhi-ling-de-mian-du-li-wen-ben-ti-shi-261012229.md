---
title: 'VibeEdit: Image Editing with Canvas Instructions'
title_zh: VibeEdit：基于画布指令的免独立文本提示图像编辑方法
authors:
- Jinjing Zhao
- Fangyun Wei
- Yitong Wang
- Xiuyu Wu
- Yunuo Chen
- Yang Yue
- Sirui Zhang
- Wenbo Wang
- Hongyang Zhang
- Dong Chen
affiliations:
- University of Sydney
- Microsoft Research
- Fudan University
- Nankai University
- Shanghai Jiao Tong University
arxiv_id: '2610.12229'
url: https://arxiv.org/abs/2610.12229
pdf_url: https://arxiv.org/pdf/2610.12229
published: '2026-10-07'
collected: '2026-10-09'
category: Multimodal
direction: 多模态生成·画布指令图像编辑
tags:
- Image Editing
- Canvas Instruction
- Multimodal Generation
- LoRA
- Reinforcement Learning
one_liner: 提出支持空间标注加短注的画布指令图像编辑范式，无需额外prompt实现5类编辑操作
practical_value: '- 电商商品图批处理场景可复用画布指令交互范式，用户直接在商品图上圈选加短注即可完成改色、换款、去杂物等操作，无需撰写复杂prompt

  - 局部生成任务可复用区域加权SFT + rubric-guided RL的训练pipeline，重点提升编辑区域准确率同时保留未编辑区域一致性，适合商品图修图、广告素材生成等场景

  - 多任务生成训练可借鉴1.55M成对编辑数据的构造方法，通过翻转编辑方向、随机渲染标注样式提升模型泛化性，降低标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文本引导图像编辑需要用户用冗长描述定位相似物体，效率低歧义高，而纯空间交互工具又缺乏灵活的语义表达能力，难以覆盖增删改移换等全类型编辑需求，亟需更自然的交互范式降低编辑门槛。

### 方法关键点
- 交互层：提出画布指令范式，支持用户直接在原图上添加圈选、涂鸦、拖拽箭头等空间标注，搭配可选短注即可表达编辑意图，无需独立文本prompt
- 模型层：基于Qwen-Image-Edit改造，采用层解耦条件编码，分别编码原图、画布指令、标注图像的语义信息，避免标注污染生成结果
- 训练层：第一阶段用区域加权SFT，给编辑区域和标注区域更高损失权重，重点优化编辑效果和标注擦除；第二阶段用rubric-guided RL，从编辑成功率、未编辑区域保留度、局部编辑质量三个维度奖励，进一步对齐用户需求
- 数据层：构造1.55M源-目标编辑对，训练时随机渲染不同笔触、字体的标注，提升模型对用户输入的泛化性

### 关键实验
在419例人工标注的相似物体编辑基准上测试，对比FireRed等最优文本引导编辑基线：VibeEdit整体VLM评分79.9，比基线高12.5分；未编辑区域PSNR 32.8dB，比基线高8.8dB，同时在增、删、属性修改、替换、移动5类编辑任务上均取得最优效果。

### 核心结论
对局部多模态生成任务，将交互语义直接锚定在空间位置上，搭配分层编码和多维度对齐训练，能同时大幅提升用户交互效率和模型生成准确率。
