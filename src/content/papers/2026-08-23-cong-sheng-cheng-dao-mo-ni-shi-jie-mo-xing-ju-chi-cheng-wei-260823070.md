---
title: 'From Generation to Simulation: How Far Are World Models from Being True Simulators?'
title_zh: 从生成到模拟：世界模型距离成为真正的模拟器还有多远？
authors:
- Tong Wang
- Huan Deng
- Mucheng Yang
- Yang He
- Xiaohui Kuang
- Gang Zhao
arxiv_id: '2608.23070'
url: https://arxiv.org/abs/2608.23070
pdf_url: https://arxiv.org/pdf/2608.23070
published: '2026-08-23'
collected: '2026-08-25'
category: Eval
direction: 世界模型能力评估 · 模拟器替代路径
tags:
- World Model
- Simulation
- Capability Audit
- Diffusion Model
- Video Generation
one_liner: 基于传统模拟器8项能力标准评测三类世界模型技术路线，明确差距并指明6个未来研究方向
practical_value: '- 做交互式Agent仿真训练时，可优先选用世界模型替代传统模拟器完成交互、可控性相关的场景验证，降低仿真搭建成本

  - 若业务仿真需要物理规律合规、长序列稳定演进、结构化实体状态查询能力，暂不建议用世界模型替代传统商用模拟器

  - 搭建电商试穿/场景化展示类生成系统时，可参考8项模拟器能力维度做选型评估，优先覆盖交互、可控性、多样性需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
生成式世界模型被广泛期望替代物理引擎、游戏引擎、强化学习环境等传统模拟器，但现有研究缺乏从模拟器视角出发的系统性能力差距评估，无法明确其落地边界。

### 方法关键点
以传统模拟器的8项核心能力（资产构建、物理引擎、交互、可控性、稳定性、状态反馈、多样性、评估指标）为统一标尺，梳理潜在动力学、视频生成、联合嵌入预测3类主流技术路线，映射2018-2026年的200篇代表性工作做横向对比。

### 关键结果数字
1. 特定场景下世界模型已在交互、可控性上实现功能替代；
2. 物理规律形式化保证、结构化状态反馈、长时序可复现演进能力远逊于传统模拟器；
3. 跨路线共性短板为状态反馈，163篇含实现的论文中仅6篇开放实体状态/物理参数查询接口。
