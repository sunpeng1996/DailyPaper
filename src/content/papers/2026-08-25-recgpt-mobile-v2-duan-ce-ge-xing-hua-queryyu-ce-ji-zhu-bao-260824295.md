---
title: RecGPT-Mobile-V2 Technical Report
title_zh: RecGPT-Mobile-V2 端侧个性化Query预测技术报告
authors:
- Lingqing Zhang
- Bin Zhang
- Weipeng Huang
- Chengfei Lv
- Chengyu Lai
- Chuxin Chen
- Dimin Wang
- Han Zhu
- Hongtao Cheng
- Jialin Zhu
affiliations:
- Alibaba
arxiv_id: '2608.24295'
url: https://arxiv.org/abs/2608.24295
pdf_url: https://arxiv.org/pdf/2608.24295
published: '2026-08-25'
collected: '2026-08-26'
category: QueryRec
direction: 端侧Query推荐 · 自适应推理与高效部署
tags:
- On-device LLM
- Query Prediction
- Adaptive Reasoning
- GRPO
- Model Compression
one_liner: 提出兼顾意图质量与推理效率的端侧个性化Query预测全链路框架，适配移动端部署
practical_value: '- 行为轨迹预处理可复用5层压缩方案：先过滤低价值被动曝光/UI噪声，再按意图强度分层截断，优先保留搜索/购买/加购等强信号，大幅降低输入token量同时保留核心意图证据

  - 端侧LLM训练可复用PT-SFT-RL-压缩分步流程：先做推荐领域增量预训练对齐Semantic ID与商品知识，SFT对齐输出规范，质量门控RL再优化推理效率，最后蒸馏量化端侧部署，平衡效果与性能

  - 推理效率优化可放弃统一长度限制，改用质量门控自适应推理：仅对质量达标候选做长度惩罚，用输入动态预算+单侧成本+乘法奖励避免短但低质Query，CoT长度中位数可从62降到14且效果无损失

  - 端侧效果不达标的case可配置端云路由策略，低置信度/多意图请求转发云端大模型处理，同时作为负例回流蒸馏端侧小模型'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
端侧个性化Query预测可将用户点击、收藏、购买等隐式行为信号映射为显式检索意图，既保护用户隐私又降低服务响应时延，但落地存在三大核心痛点：端侧获取的行为轨迹噪声多、时间跨度大，单条行为轨迹往往对应多个有效Query，统一推理策略要么对简单case浪费不必要算力，要么对复杂case分配容量不足，亟需同时兼顾Query质量与端侧执行效率的解决方案。
### 方法关键点
- 5层证据保留型行为轨迹压缩：依次经过信号过滤、行为去重、语义增强、意图分层、序列化，将日均300条原始行为压缩到100~300token，优先保留搜索、购买、加购等高价值意图信号
- 分阶段训练流水线：通用小基座恢复能力→推荐领域增量预训练对齐Semantic ID、商品语义与行为关系→SFT对齐Query输出规范与推理逻辑→质量门控GRPO RL联合优化质量与推理成本→蒸馏、量化、剪枝得到端侧部署小模型
- 质量优先自适应推理：同输入采样多组生成轨迹，仅对质量达标的候选计算推理长度惩罚，通过输入动态预算、单侧超额成本、乘法奖励+排序保护机制，避免生成短但低质的Query
### 关键结果
- 证据聚焦型短CoT相比无CoT基线，ROUGE-L从0.228提升至0.315，Jaccard从0.174提升至0.248，效果略优于五阶段完整CoT
- 完整奖励函数相比仅优化质量的RL，Query准确率从73.2%提升至78.6%，硬错误率从3.6%降至1.6%，CoT长度中位数从62token压缩到14token
- 生成Query的召回通道与现有成熟召回通道的商品重合度低，可作为补充召回源提升覆盖度
### 核心结论
高效推理不等于统一缩短推理长度，应保留决策相关证据，仅在有望提升预测Query质量时分配额外算力
