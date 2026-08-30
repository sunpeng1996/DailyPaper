---
title: 'AffectSim: A Controllable Interactive 3D Simulation Benchmark for Embodied
  Affective Perception'
title_zh: AffectSim：面向具身情感感知的可控交互式3D仿真基准
authors:
- Ke Xing
- Zhilong Wang
- Zheng Lian
- Sicheng Zhao
- Haifeng Lu
- Zhen Zhang
- Zitong Yu
- Xiaojiang Peng
- Changxin Huang
- Runhao Zeng
affiliations:
- Shenzhen MSU-BIT University
- Beijing Institute of Technology
- Tongji University
- Tsinghua University
- Great Bay University
arxiv_id: '2608.25664'
url: https://arxiv.org/abs/2608.25664
pdf_url: https://arxiv.org/pdf/2608.25664
published: '2026-08-26'
collected: '2026-08-30'
category: Agent
direction: 具身Agent · 情感感知仿真基准
tags:
- Embodied Agent
- Affective Perception
- 3D Simulation
- Benchmark
- Active Perception
one_liner: 构建观测条件可控的具身情感感知3D仿真基准 验证主动观测可显著提升情感识别性能
practical_value: '- 开发虚拟导购/直播数字人等具身交互Agent时，可参考因子化解耦设计思路，将用户情感行为与观测条件分离，构建测试场景验证不同视角/距离下的情感识别准确率

  - 迭代具身Agent主动感知策略时，可复用二阶段主动观测baseline思路，优先调整视角消除遮挡、拉近距离提升感知效果

  - 研发线下门店/商场导览Agent的情感识别模块时，可基于该基准生成多场景测试样本，降低真实数据采集成本'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有情感感知基准均为预先录制的固定样本，观测条件在推理前就已确定，无法系统研究具身感知行为对情感识别效果的影响，缺乏可控交互式仿真测试环境。
### 方法关键点
1. 提出AffectSim基准，将带情感表达的人类动作封装为可重放3D片段，支持系统调整距离、朝向、遮挡、场景几何、Agent视角等观测条件，同时保留底层行为与情感标签不变；
2. 共覆盖5类情感、57个场景，包含27647个片段，采用因子化设计解耦情感行为与观测条件，支持同一行为的可控重观测与Agent主动感知。
### 关键结果
在24种冻结感知模型配置上，最优参考观测（P-Ref）效果大幅优于初始观测（P-Init）；简单二阶段主动观测基线在21种配置上实现性能提升，开源模型Mean Macro-F1从9.89%升至11.70%，闭源模型从22.61%升至24.26%，分别填补32.0%、20.1%的P-Ref与P-Init性能差。
