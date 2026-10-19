---
title: 'HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot
  Coding Agents'
title_zh: HexaShell：面向VLM机器人编码Agent的轻量调度框架
authors:
- Hongcheng Gao
- Alex Zhou
- Jay Zhu
- Zelin Zheng
- Shijia Ge
- Xiping Li
- Di Wu
- Yazhe Wang
- Jianshu Zeng
- Xuan Shangguan
affiliations:
- HexaFuture AI
arxiv_id: '2610.23479'
url: https://arxiv.org/abs/2610.23479
pdf_url: https://arxiv.org/pdf/2610.23479
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: 机器人Agent · 工具自主迭代优化
tags:
- VLM Agent
- Tool Learning
- Robot Manipulation
- Code Agent
- Active Perception
one_liner: 基于VLM的机器人编码Agent轻量框架，通过自主迭代工具在RoboDojo达SOTA
practical_value: '- 可复用Agent工具迭代闭环设计：任务失败后仅让优化Agent诊断日志、修复小工具并固化复用，不需要重新训练基座大模型，适合电商客服Agent、选品Agent等多场景任务的快速适配，大幅降低迭代成本

  - 空间感知场景可采用多视图几何替代深度模型：在AR试穿、3D商品建模等需要空间定位的电商场景，用多视角图像+三角测量的纯几何方案比单目深度模型误差降低20~60mm，无需额外训练深度模型，减少落地复杂度

  - 轻量调度层架构可复用：harness层仅做命令翻译不做决策，所有业务逻辑下沉到工具和Agent自身，适合推荐/广告系统的Agent调度层设计，可快速切换不同基座模型、新增工具无需修改调度架构'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前机器人操作任务多由基于大量演示训练的专用策略主导，VLM Agent直接控制机器人时存在3D定位误差大、任务经验无法复用的问题，编码Agent在软件领域的「失败诊断-代码修复-能力固化」模式能否迁移到物理机器人场景、其能力边界尚未明确。
### 方法关键点
- 极薄harness层：仅将Agent输出的`robo`命令转换为机器人关节运动，不植入任何任务逻辑，Agent仅能获取3路RGB图像、相机校准参数和极简命令手册
- 双Agent工具迭代闭环：执行Agent用现有工具尝试任务，失败后同基座的优化Agent读取日志诊断问题，编写/修复带单元测试的小工具，工具固化后跨episode复用
- 纯几何3D定位：不用单目深度模型，采用多相机三角测量、平面交点计算目标坐标，单视角不足时主动移动腕部相机获取第二视角，无需额外训练感知模型
### 关键结果
在RoboDojo 42个双机械臂操作任务上测试：
- 整体成功率39.7%、进度分48.0，较SOTA学习策略VPP2高7.4个百分点，较无工具的GPT-6-Astra高17.2个百分点，达到新SOTA
- 三角测量定位比Depth Anything V2成功率高8.7个百分点，深度误差降低20~60mm
- 能力边界明显：推类任务成功率92.5%、记忆类任务65.0%，但紧插入类任务仅8.3%
> 最值得记住的结论：VLM编码Agent控制物理机器人的核心瓶颈是接触执行精度，而非推理或感知能力
