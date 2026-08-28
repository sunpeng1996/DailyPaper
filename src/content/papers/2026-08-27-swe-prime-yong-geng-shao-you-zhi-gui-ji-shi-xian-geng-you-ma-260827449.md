---
title: 'SWE-Prime: Fewer Trajectories, Better Performance'
title_zh: SWE-Prime：用更少优质轨迹实现更优编码Agent微调效果
authors:
- Dewu Zheng
- Ruizhe Ye
- Yanlin Wang
- Yang Ye
- Hongyu Zhang
- Ensheng Shi
- Xilin Liu
- Yuchi Ma
- Jianxing Yu
- Zibin Zheng
affiliations:
- Sun Yat-sen University
- Huawei Cloud Computing Technologies Co., Ltd.
- Chongqing University
arxiv_id: '2608.27449'
url: https://arxiv.org/abs/2608.27449
pdf_url: https://arxiv.org/pdf/2608.27449
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent微调 · 轨迹数据高质量筛选
tags:
- Agent SFT
- Trajectory Filtering
- Data Selection
- Process Supervision
- Coding Agent
one_liner: 提出双粒度两阶段SFT数据选择框架，仅用10%成功轨迹训练编码Agent性能超全量数据
practical_value: '- 做Agent SFT时不要直接复用所有成功轨迹，可先做轨迹级过滤：从过程合规性（如工具调用成功率、冗余操作占比、作弊行为）、结果质量、数据代表性三个维度打分筛选，用10-20%优质子集即可达到甚至超过全量训练效果，大幅降低训练成本。

  - 长对话/长轨迹SFT可复用段级过滤思路：将连续步骤按语义切分为独立段，仅对高贡献、可学习、无风险的段计算损失，保留全量上下文保证连贯性，同时避免无效行为给模型引入噪声。

  - 多类别轨迹选择时可搭配语义Embedding聚类后按簇选TopK的策略，避免优质样本集中在少数任务类型，保证训练数据覆盖度，防止模型过拟合到特定场景。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有编码Agent SFT仅基于任务成功与否筛选训练轨迹，然而成功轨迹往往包含无效操作、冗余步骤、风险行为，直接用于训练会引入噪声，教给模型不合理的问题解决模式，亟需更精细的高质量SFT数据筛选方案。

### 方法关键点
- **阶段1 轨迹级过滤**：从3个维度综合打分筛选优质轨迹：1）过程质量：检查是否符合观察-编辑-验证标准流程、工具调用成功率、无连续冗余操作、无Git信息泄露等作弊行为；2）结果质量：对比生成补丁与基准补丁的文件/行修改范围，修改范围越贴合基准得分越高；3）数据代表性：对问题描述做Embedding聚类，每个簇内按轨迹得分选TopK，保证不同类型问题的覆盖度。
- **阶段2 段级过滤**：首先用边界感知滑动窗口将长轨迹切分为语义连贯的行为段，再按「对最终结果的贡献度、局部可学习性、是否存在风险行为」3个维度给段打分，仅对得分超过阈值的段计算SFT损失，其余段保留为上下文不参与损失计算，兼顾连贯性与监督信号质量。

### 关键实验
在SWE-Bench Pro、SWE-Bench Verified两个基准，3款不同基座模型上验证：仅用10%筛选后的轨迹训练，相比全量成功轨迹训练，在两个基准上分别取得最高12.2%、24.2%的相对性能提升，同时工具调用成功率更高、冗余操作减少，平均交互轮次降低4.1-12.7轮。

### 核心结论
Agent SFT的效果不取决于成功轨迹的数量，而取决于轨迹的质量、代表性与内部行为的可学习性。
