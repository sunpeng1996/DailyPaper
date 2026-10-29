---
title: When Should We Intervene at Test Time?
title_zh: 测试阶段何时触发模型自适应干预？
authors:
- Jiahao Zhang
- Xinling Wen
- Liangliang Li
- Yu Chen
affiliations:
- Zhengzhou University of Aeronautics
- Xi'an University of Technology
arxiv_id: '2610.37658'
url: https://arxiv.org/abs/2610.37658
pdf_url: https://arxiv.org/pdf/2610.37658
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 测试时自适应 · 干预决策控制
tags:
- Test-time Adaptation
- Model Intervention
- Label Efficiency
- Online Control
- Distribution Shift
one_liner: 提出PORTAL轻量控制器，仅用少量标注即可决策测试时是否触发模型干预，避免干预带来的效果劣化
practical_value: '- 线上推荐/搜索模型做实时干预（如在线归一化统计量更新、小批次LoRA微调）时，可复用PORTAL的干预触发逻辑，避免全量干预导致的部分流量效果劣化

  - 线上少量标注资源分配可复用PORTAL的查询停止策略，当预期精度增益无法覆盖标注成本时停止采样标注，有效降低标注成本

  - 业务流量分布发生漂移时，可借鉴PORTAL的周期性标注校验机制，及时刷新干预策略适配新分布，避免长期效果衰减'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
已有的测试时自适应策略全量触发时存在批次级效果波动，可能在部分批次提效、部分批次劣化，平均精度无法指导干预时机选择，全量标注成本过高不可落地。
### 方法关键点
提出PORTAL控制器：1）将不同干预/无干预策略作为候选集，所有候选在当前反馈返回前固定预测结果，单样本标注可同步评估所有候选；2）优先向有概率超过当前最优候选的方向分配标注资源；3）当剩余标注无法改变最优选择或增益无法覆盖标注成本时停止查询；4）新增周期性标注校验刷新历史策略有效性，收集的标注同时用于优化未来批次的候选策略。
### 关键结果
实验证明，该控制器可将整体精度下跌的干预策略转化为选中批次的有效提优，避免输入顺序变化导致的严重失效；固定策略表现良好时仅需极少标注即可维持效果，收集的标注同时可训练更强的未来候选策略，几乎可完全覆盖候选的精度增益。
