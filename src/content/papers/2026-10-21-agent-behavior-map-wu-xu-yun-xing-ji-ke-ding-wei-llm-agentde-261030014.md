---
title: 'Agent Behavior Maps: Locating Agents by What They Would Do, Without Running
  Them'
title_zh: Agent Behavior Map：无需运行即可定位LLM Agent的行为特征
authors:
- Shota Fujikawa
- Takuya Tamura
- Kosuke Akimoto
- Daichi Haraguchi
- Masafumi Oyamada
affiliations:
- The University of Tokyo
- NEC Corporation
arxiv_id: '2610.30014'
url: https://arxiv.org/abs/2610.30014
pdf_url: https://arxiv.org/pdf/2610.30014
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent行为表征与相似性度量
tags:
- LLM-Agent
- Behavior-Similarity
- Performance-Prediction
- Off-Policy-Evaluation
- Harness-Optimization
one_liner: 基于共享参考轨迹的对数似然构建Agent行为坐标，无需环境rollout即可预测性能匹配行为相似性
practical_value: '- 电商/导购Agent选型阶段，可预先收集少量业务场景的真实交互轨迹作为参考集，新Agent仅需做前向计算打分即可快速筛选性能达标、行为路径符合预期的候选，无需全量在线/仿真跑测，大幅降低选型成本

  - 优化Agent的harness组件（如上下文窗口、规划模块、思维链模块）时，可复用单组件位移可加性结论，无需枚举所有组件组合跑测，仅通过单组件的坐标位移加和即可预测组合效果，减少90%以上的测试量

  - 高频迭代的推荐Agent（如个性化内容生成Agent、搜索query改写Agent）的离线评估，可将坐标距离作为行为一致性的代理指标，快速判断新版本Agent和线上版本的行为差异，避免上线后出现不符合预期的操作'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent的评估不仅需关注成功率，还需衡量动作序列、工具选择等行为特征，但每款新Agent（含不同LLM+harness组合）都需要全量环境rollout才能采集行为数据，成本极高，尤其是Agent组合爆炸的场景下效率极低，亟需无需运行即可量化Agent行为相似性的方法。
### 方法关键点
- 预先生成一批固定的共享参考轨迹，目标Agent仅通过teacher forcing计算参考轨迹中每个动作的对数似然，减去自身均值后得到标准化的行为坐标，无需和环境交互
- 推导了坐标距离与轨迹KL散度的误差边界，拆解为局部近似、参考分布 mismatch、中心化、采样四类误差，明确步级坐标误差随轨迹长度线性增长，远优于轨迹级的平方增长
- 支持harness组件的位移可加性计算，单个harness组件带来的坐标位移可加和，预测多组件组合后的行为坐标
### 关键结果
- 实验覆盖100款开源LLM、4个主流Agent测试环境，对比模型大小、模型家族、平均对数似然三类baseline
- ALFWorld环境下成功率预测Pearson r达0.88，远超模型大小baseline的0.63；坐标距离与真实轨迹KL的Spearman相关系数达0.95
- 坐标近邻的Agent行为相似性效应量是参数大小近邻的2倍左右；双harness组件组合的位移预测余弦相似度中位数达0.90
### 核心结论
无需运行Agent，仅通过其在固定参考轨迹上的对数似然分布，就能准确捕捉其行为相似性和下游性能，大幅降低Agent选型和评估的成本
