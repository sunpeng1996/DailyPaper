---
title: 'MJev-Spatial: System One Spatial Intelligence via Native Attention Matching'
title_zh: MJev-Spatial：基于原生注意力匹配的系统1空间智能模型
authors:
- Luozheng Qin
- Yuhan Zhu
- Changhai Zhou
- Qian Qiao
- Jun Gao
- Yuhua Zhou
- Harry Zhang
- Xiangyu Zeng
- Yuxuan Liu
- Kaijie Chen
affiliations:
- 复旦大学
- MindLab
arxiv_id: '2610.22276'
url: https://arxiv.org/abs/2610.22276
pdf_url: https://arxiv.org/pdf/2610.22276
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 空间感知决策优化
tags:
- VLM
- Spatial Intelligence
- System 1
- Attention Matching
- Inference Acceleration
one_liner: 将三类空间理解任务统一为无额外参数的分类范式，精度领先同时推理速度较自回归基线提升5.6倍
practical_value: '- 可复用「紧凑输出空间任务转候选分类」的思路，替代自回归生成，用于电商虚拟场景商品摆放判定、多模态商品属性识别等任务，大幅降低推理延迟

  - 直接复用预训练模型最后一层Q/K投影做候选打分，无需新增预测头，可快速适配冷启动多模态分类任务，节省训练和部署成本

  - 训练异构多模态数据时，采用全局长度分组+跨GPU负载均衡策略，可直接提升训练吞吐量30%以上，适合多模态推荐、搜索模型的训练流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM处理空间理解任务时依赖自回归文本生成，需额外答案解析步骤，推理延迟高，且将任务目标学习与文本格式学习耦合，引入不必要的监督开销；而空间任务输出空间本身高度紧凑（有限选项、标量、2D点），完全可以采用更高效的决策范式实现。
### 方法关键点
- 统一分类框架：将选项选择、数值估计、点定位三类空间任务全部转化为有限候选集的分类任务，数值和点预测采用由粗到细的多阶段分类，避免候选集爆炸
- 原生注意力打分：直接复用主干模型最后一层预训练的Q、K投影计算候选得分，不新增任何参数，推理时单次前向即可完成单阶段决策，无需生成答案token
- 高效训练策略：用teacher forcing联合监督所有粗到细阶段的损失，全局长度分组+跨GPU负载均衡处理异构数据的长度、计算量差异，提升训练吞吐量
- 细节优化：数值预测用对数间隔粗bin+线性细bin平衡范围和精度，点预测每阶段裁剪目标区域重新编码补充局部视觉信息，多点预测通过概率树扩展实现无需额外训练
### 关键实验
基于Qwen3.5-4B训练，训练集为12.3M转化后的空间任务QA对，在12个空间基准上对比7个主流自回归VLM基线：整体得分65.64%位列第一，12个基准中7个排名第一，全部12个基准均优于未修改的自回归基线；推理延迟仅160.6ms，比最快的自回归基线快2.5倍，比原生Qwen3.5-4B快5.6倍；训练调度策略较原batch方案提升吞吐量30.8%。
### 核心洞察
对于输出空间有限的决策类任务，直接复用预训练模型的原生匹配能力做分类，相比自回归生成可同时实现精度提升和推理加速。
