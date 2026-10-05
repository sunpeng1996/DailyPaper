---
title: 'Looping Beyond Twice: A Scalable Recipe for Looped Mixture-of-Experts'
title_zh: 突破双循环限制：可扩展的循环混合专家（Looped MoE）实现方案
authors:
- Di He
- Pengxiang Li
- Da Chang
- Qingyan Meng
- Lu Yin
- Shiwei Liu
affiliations:
- Shenzhen Institutes of Advanced Technology, CAS
- Peng Cheng Laboratory
- University of Chinese Academy of Sciences
- The Hong Kong Polytechnic University
- University of Surrey
arxiv_id: '2610.01153'
url: https://arxiv.org/abs/2610.01153
pdf_url: https://arxiv.org/pdf/2610.01153
published: '2026-09-30'
collected: '2026-10-05'
category: LLM
direction: 大语言模型 · MoE 循环缩放优化
tags:
- MoE
- Looped Transformer
- Scaling Law
- LLM Training
- Parameter Efficiency
one_liner: 针对循环MoE难以突破2次迭代的痛点，提出LOOM方案实现9-12次循环的稳定高效缩放
practical_value: '- 业务侧用小参数MoE LLM做推荐文案生成、query理解/改写时，可引入LOOM的循环机制，不增加核心参数的前提下通过提升循环次数优化效果，严格控制推理成本

  - 多专家排序/召回模型遇到专家利用同质化问题时，可复用「不同迭代步配独立router、专家权重共享」的trick，仅增加极少量router参数就能大幅提升专家利用效率

  - 所有循环类Transformer的落地训练可直接复用分段反向传播（K=3）策略，实测可降低40%+显存占用、缩短50%训练时间，同时提升训练稳定性

  - 多轮迭代的Agent推理流程可复用「残差按循环次数缩放、每步重注入初始输入embedding」的trick，避免多轮交互后的状态漂移问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Looped Transformer可通过复用Transformer块在不增加参数的前提下提升有效深度，是独立于模型尺寸、训练数据之外的新缩放轴，但现有Looped MoE方案普遍最多只能支持2次循环，继续增加循环次数会出现性能不升反降的问题：一是深度诅咒，反复迭代导致残差积累、隐状态方差爆炸、表征漂移；二是专家选择坍塌，共享router在不同循环步路由到相同专家，额外计算无法带来有效收益，亟需可扩展的方案突破双循环限制。
### 方法关键点
- 稳定循环机制：残差更新按γ=λ/(H√M)缩放控制方差增长，每轮循环按gt=λ/(t√M)重注入原始输入embedding，锚定隐状态避免漂移
- 多样化计算设计：每轮循环配置独立router（专家权重共享）避免路由同质化，新增Loop Residual用EMA聚合跨轮和本轮注意力输出，保留历史迭代信息
- 训练工程优化：采用分段反向传播，每3次循环做一次梯度回传并切断前面的梯度，大幅降低显存占用，提升训练稳定性
### 关键结果
在100M-1.7B参数MoE模型上基于FineWeb-Edu数据集训练，对比无循环基线、原生循环MoE等方案：
- 近等FLOPs下，700M模型5次循环最优，困惑度从18.36降至16.54，零样本平均准确率从38.84%提升至39.53%
- 无FLOPs限制下，1.7B模型9次循环最优，困惑度从9.62降至7.77，零样本平均准确率从42.4%提升至47.7%，稳定支持最多12次循环
### 核心结论
循环深度是MoE LLM的高性价比缩放轴，通过稳定循环状态+保障跨轮计算多样性两个核心优化，可突破传统2次循环的上限，在不增加核心参数的前提下显著提升模型效果。
