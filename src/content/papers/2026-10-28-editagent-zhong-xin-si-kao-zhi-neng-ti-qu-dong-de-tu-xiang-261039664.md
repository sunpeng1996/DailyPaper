---
title: 'EditAgent: Rethinking Agentic Image Editing'
title_zh: EditAgent：重新思考智能体驱动的图像编辑范式
authors:
- Haiyang Xu
- Tianyu Wang
- Jialu Li
- Jiteng Mu
- Yuanjun Xiong
- Jianming Zhang
- Zhuowen Tu
- Mingze Xu
affiliations:
- UC San Diego
- Adobe Research
arxiv_id: '2610.39664'
url: https://arxiv.org/abs/2610.39664
pdf_url: https://arxiv.org/pdf/2610.39664
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: 多模态Agent · 智能图像编辑
tags:
- Agent
- VLM
- Image Editing
- Reward Model
- Data Engine
one_liner: 通过扩展智能体动作空间与裁判观测空间，实现无需微调奖励模型的SOTA多轮图像编辑智能体
practical_value: '- 电商商品图/营销素材编辑场景的Agent可直接复用架构：不用依赖单模型顺序迭代，并行调用通用编辑器+专用工具（如物体移除、调色、裁剪算子）生成多候选，错误率更低，VLM调用次数最多减少50%

  - 生成式内容自动质检可直接复用观测增强方案：给VLM输入候选结果时附带任务相关可量化证据（如编辑区域特写、色值/几何参数变化、程序校验结果），无需微调专用奖励模型，就能超过现有微调奖励模型的判断准确率

  - 复杂Agent能力可快速落地线上：Agent生成的所有验收合格的会话数据可直接作为训练集，蒸馏轻量端侧模型，大幅降低线上推理成本，同时避免低质量训练样本导致的效果退化

  - 编辑类任务优先采用源图并行生成策略：对比顺序迭代编辑，直接从源图生成多候选的模式可避免误差累积，专家偏好度达78.5%，适合电商商品图修图、营销素材二次加工等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent图像编辑框架动作空间局限于少数通用工具，裁判仅靠原始图、编辑图、指令做单点判断，通用编辑器在42.7%的场景下出不了可用结果，微调的专用奖励模型也无法在所有编辑类型上都表现可靠，多轮顺序迭代还容易累积误差，复杂编辑任务的效果瓶颈明显。

### 方法关键点
1. 扩展动作空间：每个编辑步骤路由到通用编辑器+8类专用工具（局部编辑、物体移除/移动、光度/几何算子、风格滤镜等），并行生成多个候选；
2. 扩展观测空间：每个候选附带校验证据（编辑区域特写、变化图、色值/几何参数、程序校验结果），off-the-shelf VLM做列表式对比裁判，无需微调；
3. 多轮编辑增加历史校验环节，避免后序步骤覆盖之前的编辑效果；
4. 所有验收的编辑会话直接作为数据引擎，产出高质量训练样本蒸馏小模型。

### 关键结果
在EdiVal、Complex-Edit、ComplexBench-Edit三个基准上，基于Qwen-Image-Edit和FLUX.2-klein-9B两个底座，EdiVal第3轮得分最高提升4.94分；专家偏好并行生成模式的非平局对比占比达78.5%，裁判调用次数减半；带证据的VLM裁判准确率比最优微调奖励模型EditScore-72B高8分；用产出的25.7K合格会话训练底座，效果比直接用底座生成的数据高2分左右。

### 核心结论
对于需要保留原始信息的生成编辑任务，扩大动作空间+给裁判足够可解释证据，比反复迭代单模型、微调专用奖励模型的性价比高得多。
