---
title: Adapting Knowledge Graphs for Behavior Denoising in Sequential Recommendation
title_zh: 适配知识图谱的序列推荐行为去噪方法
authors:
- Zichun Jin
- Zihan Zhou
- Yinan Liu
- Bin Wang
- Xiaochun Yang
affiliations:
- Northeastern University, Shenyang, China
arxiv_id: '2608.21243'
url: https://arxiv.org/abs/2608.21243
pdf_url: https://arxiv.org/pdf/2608.21243
published: '2026-08-21'
collected: '2026-08-24'
category: RecSys
direction: 序列推荐 · 知识图谱辅助行为去噪
tags:
- Sequential Recommendation
- Knowledge Graph
- Behavior Denoising
- Training Calibration
- Offline Processing
one_liner: 基于知识图谱结构匹配生成样本级留存系数，离线完成去噪无需修改推荐主干与推理逻辑
practical_value: '- 可复用结构匹配去偏思路，计算KG关联度时加入热度、度数匹配的对照组，解决高连通/热门item的置信度高估问题

  - 所有KG侧计算、留存系数生成全离线完成，无需修改现有推荐主干模型，推理时也不需要接入KG，落地成本极低

  - 生成的留存系数可直接复用：既用来加权历史交互embedding，也用来加权训练目标损失，无需额外调参即可适配现有序列推荐/去噪模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
序列推荐依赖用户历史交互预测下一个物品，但真实业务日志混有临时需求、误触、随机探索等噪声交互，会扭曲用户历史表征、引入不可靠的训练监督。现有去噪方法仅基于交互共现、时序关系或模型预测判断噪声，缺乏物品间显式关系证据；直接引入知识图谱（KG）做判断的话，高热度、高KG度数的物品天然有更多连接，会导致交互可靠性估计向热门物品偏倚。
### 方法关键点
- 两步结构匹配校准：第一步用与当前序列结构属性（热度、KG度数、连接状态）匹配的空上下文做对照，筛选出显著高于基线的关系路径，构建样本专属的局部KG视图；第二步用与待评估交互结构属性匹配的参考物品做对照，校准该交互在局部KG视图下的支持度，生成0-1区间的留存系数
- 留存系数双用途：训练时既用系数加权历史交互的embedding输入序列编码器，也用系数加权目标样本的交叉熵损失
- 全流程无侵入：所有样本的留存系数仅用训练集交互和固定KG离线计算，完全不修改推荐主干架构，推理时不需要访问KG
### 关键实验结果
在Steam Games数据集（2.5w用户、4k物品、32.8w交互、46.2w KG三元组）上测试，覆盖4类基线：标准序列模型SASRec、带去噪机制的STEAM/BirDRec/SSDRec，所有指标均获得提升：SASRec的N@10从61.3提升至74.3，涨幅21.2%；STEAM的H@5从85.1提升至96.2，涨幅13%；已带内置去噪的模型也获得稳定的效果增益。
### 核心结论
用KG做推荐行为去噪不需要将KG表征注入推荐主干，离线校准得到的样本级权重就能以极低落地成本带来全域效果收益。
