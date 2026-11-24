---
title: 'Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models'
title_zh: Fast-JEPA：优化隐式世界模型规划的成功率-延迟帕累托边界
authors:
- Yao Zhang
- Bin Yu
- Shijie Lian
- Haishan Liu
- Changti Wu
- Yu Wu
- Kai Chen
affiliations:
- Wuhan University
- Harbin Institute of Technology
- Huazhong University of Science and Technology
- Nanjing University
- DeepCybo
arxiv_id: '2611.25927'
url: https://arxiv.org/abs/2611.25927
pdf_url: https://arxiv.org/pdf/2611.25927
published: '2026-11-18'
collected: '2026-11-24'
category: Agent
direction: Agent 低延迟世界模型规划优化
tags:
- World Model
- JEPA
- Low Latency
- Planning
- Pareto Optimization
one_liner: 重构世界模型预测计算流程，无需递归状态推演实现低延迟高准确率规划
practical_value: '- 生成式推荐/多步决策场景可复用「终端直接预测」思路：评估候选动作/物品序列效果时，无需递归模拟每一步状态转移，直接预测最终转化/留存目标，可大幅降低线上推理延迟，适配高QPS业务场景

  - 搜索/重排模块可借鉴「基准提案+局部精细搜索」架构：先通过规则/轻量模型生成高置信初始候选集，再用CEM等方法在小范围做精细化调优，平衡效果与算力消耗，避免全量搜索的资源浪费

  - 线上效果评测可参考DynaGoal设计思路：新增动态目标漂移、响应延迟约束、OOD环境等评测维度，更贴合真实业务中用户兴趣突变、流量波动、算力不足等实际场景，提升评测的业务相关性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于隐式世界模型的规划依赖递归状态推演评估候选动作序列，线上推理延迟高，难以适配动态环境、执行deadline等真实落地场景，亟需在不损失成功率的前提下降低规划延迟，优化成功率-延迟帕累托边界。
### 方法关键点
- 分层预测设计：动作构造阶段用锚定初始观测的中间预测生成高置信初始提案，候选评估阶段直接批量预测完整动作序列的终端状态，避免递归推演的重复计算
- 提案引导的轻量搜索：基于初始提案用CEM在局部采样候选，保留初始提案与历史最优候选，保证搜索效率下限，无需大范围随机采样
- 轻量化联合训练：世界模型同时监督多horizon的锚定预测结果，动作生成模型同时用中间状态、终端目标两个维度监督，无需额外定制特殊网络结构
### 关键实验
在PushT、Reacher、Cube、TwoRoom四个标准控制任务上，对比INTACT等10+基线，平均成功率达96.50%，规划延迟仅10.88ms，比SOTA INTACT快2.41倍；在自研动态OOD基准DynaGoal-Shift、DynaGoal-Deadline上，平均成功率分别达73.83%、87.67%，均大幅领先所有基线。
### 核心结论
预测计算要按需分配：动作构造阶段用中间预测保证合理性，候选评估阶段用直接终端预测降低延迟，两者结合可在几乎不损失效果的前提下大幅降低推理成本。
