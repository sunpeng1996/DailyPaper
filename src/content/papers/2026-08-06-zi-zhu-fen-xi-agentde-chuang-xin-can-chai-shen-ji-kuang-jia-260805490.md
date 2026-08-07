---
title: 'Innovation-Residual Auditing of Autonomous Analysis Agents: Localization,
  Detection Limits, Error Control, and Identifiability'
title_zh: 自主分析Agent的创新残差审计框架：定位、检测限与错误控制
authors:
- Ahmed Hassoon
- Mark Dredze
affiliations:
- Johns Hopkins University
arxiv_id: '2608.05490'
url: https://arxiv.org/abs/2608.05490
pdf_url: https://arxiv.org/pdf/2608.05490
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 自主Agent 执行轨迹错误审计
tags:
- Agent Audit
- Trajectory Anomaly Detection
- Error Localization
- FDR Control
- Statistical Guarantee
one_liner: 构建无标注错误下自主分析Agent轨迹审计的完整统计理论体系，覆盖定位、错误控制与检测边界
practical_value: '- 电商/广告场景的任务型Agent（如导购Agent、自动投放Agent）可直接复用该无监督审计范式，仅用成功执行轨迹训练即可定位错误步骤，无需标注错误样本，大幅降低标注成本

  - 推荐/搜索链路的异常检测场景可复用文中的FDR控制流程，根据业务可接受的误报率设置阈值，避免大量假阳性告警干扰运维

  - 多horizon残差设计可直接迁移到渐变异常检测任务（如用户兴趣漂移、推荐链路性能退化），通过设置1/4/16等多阶窗口兼顾单点突变和渐变异常的检测

  - 检测下限结论可指导异常检测的embedding设计：无需盲目堆叠训练数据，优先降低有效维度并保留异常相关的特征维度，可大幅提升检测灵敏度'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前LLM驱动的自主Agent已可端到端完成数据分析、任务执行等全流程操作，中间步骤无需人工审核，一旦输出错误很难定位到具体执行步骤；现有无标注错误的审计方案缺乏完整的统计理论支撑，无法量化误报率、检测边界等核心指标，难以落地到对可靠性要求高的业务场景。
### 方法关键点
1. 采用单类学习范式，仅在成功执行轨迹上训练预测模型，用one-step创新残差作为步骤异常评分，避免前期错误扩散到后续正确步骤的评分，实现精准定位
2. 支持多预测horizon的残差设计，短窗口适配单点突变错误检测，长窗口适配渐变式错误检测
3. 提出不依赖模型正确假设的FDR控制流程，支持任意轨迹内依赖下的假阳性控制，同时给出了审计样本选择偏差的敏感性分析方法
4. 推导了通用检测下限，明确高维embedding场景下检测能力的核心约束是embedding维度而非训练数据规模
### 关键结果数字
- 当embedding维度d=256时，最大坐标评分对单维度稀疏扰动的检测灵敏度比全维度chi-square评分高3.3倍
- 训练数据规模百倍增长仅能将检测下限降低不到2%，瓶颈完全由embedding维度决定
- e-BH错误控制方法避免了传统Benjamini–Yekutieli方法的调和数惩罚，在短轨迹（40步以内）下的检测效率提升3倍以上

**最值得记住的结论**：无监督Agent执行轨迹审计的核心瓶颈是embedding维度，合理设计评分函数和错误控制流程可在无错误标注的前提下实现工业级可靠的错误定位
