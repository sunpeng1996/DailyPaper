---
title: 'Dual Exam: Controlled Evaluation of Multimodal Agents and World Models'
title_zh: Dual Exam：多模态Agent与世界模型的可控评估框架
authors:
- Zhefan Rao
- Meng Chu
- Xuan Zhang
- Jingfan Chen
- Guohao Cai
- Runyi Li
- Shiyi Du
- Ning Lu
- Xu Huang
- Zhixuan Chen
affiliations:
- The Hong Kong University of Science and Technology
- National University of Singapore
- The Hong Kong Polytechnic University
- The University of Tokyo
- Carnegie Mellon University
arxiv_id: '2610.31066'
url: https://arxiv.org/abs/2610.31066
pdf_url: https://arxiv.org/pdf/2610.31066
published: '2026-10-21'
collected: '2026-10-26'
category: Eval
direction: 多模态Agent与世界模型 可控评测框架
tags:
- Multimodal Agent
- World Model
- Evaluation Framework
- Benchmark
- Controlled Assessment
one_liner: 提出双轨可控评估框架，分别在固定环境/固定动作下评测多模态Agent与世界模型能力
practical_value: '- 搭建电商导购Agent、商品仿真推荐等MA-WM耦合系统时，可复用双轨分离评测思路：固定环境测Agent决策能力、固定动作测WM仿真准确性，避免耦合故障无法定位

  - 电商多模态Agent选型时可参考本评测的能力维度划分：行动序列规划、网页交互、多模态理解等，针对性评测业务场景所需能力，无需盲目参考通用排行榜

  - 世界模型用于虚拟试穿、家居摆放仿真等电商场景时，需优先验证动作响应的状态一致性，避免动作输入后生成结果违反业务约束（如商品款式/颜色突变）'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多模态Agent（MA）与世界模型（WM）耦合系统的端到端故障无法定位是核心迭代瓶颈：现有评估多测试耦合端到端效果，无法区分失败源于Agent决策错误还是WM仿真偏差；先导实验显示某MA-WM配对在10个场景150个case上任务成功率为0，且无法定位故障来源。

### 方法关键点
- 双轨分离评测设计：Agent评测轨固定参考环境响应机制，仅测Agent的行动选择、错误恢复、任务完成能力；WM评测轨固定动作干预序列，仅测WM的状态演化一致性、动作响应准确性
- 覆盖四大领域：物理、数字、社会、科学，共15类Agent评测任务、8类WM评测场景，所有任务明确初始状态、约束、验证规则，基于实际执行证据打分而非模型自报告
- 差异化聚合规则：Agent Index按任务数量加权聚合，WM Overall按场景均分聚合，两个轨道分数不直接可比

### 关键实验
- Agent评测：10款主流多模态模型在1088个任务上测试，GPT 6 Astra获得最高Agent Index 31.3，各模型能力存在明显领域差异，无模型在所有类别领先
- WM评测：16款世界模型在400个case上测试，GPT-Image-2获得全配置最高Overall 21.7，Web、游戏等数字场景是所有WM的共同短板

### 核心结论
MA-WM耦合系统的稳定性依赖双方能力达标，仅测端到端效果无法支撑迭代，必须先做组件级可控评测定位能力短板
