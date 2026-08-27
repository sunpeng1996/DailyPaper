---
title: 'D^3-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation'
title_zh: D³-MOPD：面向高效多教师蒸馏的自适应动态域调度方法
authors:
- Zechen Sun
- Zhiwei Zhang
- Fei Zhao
- Juntao Li
- Mu Chuan
- Huayu Deng
- Guojian Zhan
- Wenliang Chen
- Yao Hu
- Min Zhang
affiliations:
- AllSpark Team
arxiv_id: '2608.24987'
url: https://arxiv.org/abs/2608.24987
pdf_url: https://arxiv.org/pdf/2608.24987
published: '2026-08-24'
collected: '2026-08-27'
category: Training
direction: 大模型训练 · 多教师蒸馏调度
tags:
- Knowledge Distillation
- Multi-Teacher Distillation
- Dynamic Scheduling
- Training Efficiency
- LLM Training
one_liner: 复用训练原生反向KL信号实现零开销动态域调度，提升多教师蒸馏效果与训练效率
practical_value: '- 做多场景/多域LLM微调（电商搜推广多场景、Agent多技能蒸馏）时，无需固定数据配比，可复用各域已有loss/反向KL信号动态调整采样权重，零修改核心训练逻辑，同时提效果省算力

  - 可直接复用调度核心trick：「剩余gap（当前loss/初始loss）* 下降速度」计算复合得分，加温度softmax+最低采样率保底，既能倾斜资源给学得慢但有潜力的域，又防止灾难性遗忘

  - 做多技能Agent蒸馏（工具调用、文案生成、用户理解等单技能老师蒸馏到端侧小模型）时可直接套用这套方案，4B到35B规模均生效，最高可省3倍训练步数'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多教师在线蒸馏（MOPD）普遍采用固定域数据配比，忽略不同域收敛速度差异极大的问题，导致快收敛域浪费算力、慢收敛域训练不足，最终学生模型与老师的性能缺口大，训练效率低。

### 方法关键点
- 新增异步独立Watcher进程，复用训练过程中已计算的每个域的reverse-KL信号，无需修改核心训练逻辑，无额外训练开销
- 复合得分由两个维度相乘得到：剩余gap（当前平滑KL/初始KL，归一化解决不同域KL绝对值差1-2个数量级的问题）、下降速度（最近R个窗口的KL平均下降率，剪枝到0避免无效分配）
- 得分经带温度的softmax+每个域最低采样率ϵ映射为采样比例，再给每个batch加小幅抖动，避免固定配比导致的梯度弱、收敛差问题

### 关键实验
用Qwen3.6-35B-A3B做学生，蒸馏Math、Code、指令跟随、工具调用4个域的专家老师，对比vanilla MOPD基线：
- 最终填平97%的学生-老师平均性能缺口，基线仅63%，7个测试基准中有3个超过单领域专家老师
- 达到基线的峰值性能仅需47步，比基线的143步快约3倍
- 4B小模型场景下效果同样优于基线，还能超过复合专家能力上限

### 最值得记住的一句话
多域蒸馏不需要复杂调优固定配比，复用训练过程中已经产生的loss信号做动态调度，就能用更低算力拿到更好效果。
