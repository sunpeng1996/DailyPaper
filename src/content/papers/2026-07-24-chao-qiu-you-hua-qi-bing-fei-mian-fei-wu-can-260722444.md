---
title: Hyperball May Not Be a Free Lunch
title_zh: 超球优化器并非“免费午餐”
authors:
- Yihao Xiao
- Jialong Sun
- Zitian Gao
- Zeming Wei
- Chutian Wang
- Ran Tao
- Jiaye Teng
- Bryan Dai
affiliations:
- IQuest Research
- Peking University
- Sun Yat-sen University
- Shenzhen University of Advanced Technology
- Shanghai University of Finance and Economics
arxiv_id: '2607.22444'
url: https://arxiv.org/abs/2607.22444
pdf_url: https://arxiv.org/pdf/2607.22444
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: 大模型训练·优化器性能调优
tags:
- Optimizer
- Hyperball
- Learning Rate Scheduling
- Model Training
- Muon
one_liner: 拆解超球优化器性能来源，证明其效果来自学习率动态而非更新方向的固有优势
practical_value: '- 训练LLM4Rec、推荐多模态大模型时，若使用超球类优化器，不能省略学习率调度策略，恒定角速度设置无法避免调参需求

  - 超球优化器早期收敛慢的问题可通过更激进的学习率衰减提速，但需平衡后期性能损伤，适合对训练速度要求高的小模型迭代场景

  - 优化器对比实验中需严格控制有效步长等无关变量，避免误将学习率动态的差异归因于优化器更新方向的固有优势'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
超球类优化器在尺度不变深度网络大规模训练中表现优异，但性能优势来源不明确，业界普遍认为其可免除学习率调度调优成本。
### 方法关键点
1. 从连续参数状态的角位移出发，推导融合参数-更新夹角、参数范数、更新范数的角度有效学习率，证明传统范数度量是参数-更新正交场景下的特例；
2. 将优化器更新拆解为径向、切向分量，量化分析径向更新对单步角位移的影响；
3. 设计仅修改学习率调度的控制变量实验，隔离更新方向与有效步长的作用。
### 关键结果
1. 径向分量对角度有效学习率的直接影响不足10%，无法解释MuonH早期收敛慢于MuonWD、后期反超的现象；
2. 两类优化器的性能差异核心来自有效步长的演化，而非超球带来的更新方向固有优势；
3. 激进学习率衰减可将MuonH早期训练速度提升30%，但会导致最终预训练效果下降2%~5%；
4. 恒定角速度设置无法消除学习率调度需求，合理调参才能释放超球优化器的全部潜力。
