---
title: Personal-Agent Mediated Recommendation with Cross-Platform User History
title_zh: 基于跨平台用户历史的个人Agent介导推荐
authors:
- Yu Xia
- Jiangfan Zhang
- Jun Xiao
- Julian McAuley
- Xiangjun Fan
affiliations:
- University of California San Diego
- Meta AI
arxiv_id: '2610.07588'
url: https://arxiv.org/abs/2610.07588
pdf_url: https://arxiv.org/pdf/2610.07588
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: Agent介导推荐 · 跨平台用户建模
tags:
- Personal_Agent
- Cross_Platform_Recommendation
- LLM4Rec
- RLHF
- Mediated_Recommendation
one_liner: 提出用户侧个人Agent介导推荐范式、配套基准和PAMO训练方法，用跨平台历史优化平台推荐结果
practical_value: '- 业务落地可参考「平台初排+用户侧Agent重排」的架构，无需改造现有平台推荐 pipeline，跨平台数据仅保留在用户侧，符合隐私合规要求，改造成本极低

  - 训练基于独有特征（跨站行为、隐私数据等）的LLM重排器时，可复用PAMO的反事实mask思路：mask掉独有特征后对比输出概率差，度量预测对该特征的依赖度，优化奖励分配，减少无依据的错误调整

  - 跨域/跨平台推荐评测可借鉴MediateRec的信息边界设计，分开计算平台原生效果和跨域数据带来的新增增益，避免AB测试时将平台本身的效果误算为新方案的贡献'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
传统推荐为平台中心化架构，仅能使用站内用户行为数据，用户侧授权的个人LLM Agent可获取跨平台历史，但现有Agent推荐方案均为平台侧部署，未解决「何时信任平台全局协同信号、何时用跨平台历史调整排序」的权衡问题，直接重排易出现大量有害覆盖，删除平台原本排对的优质内容。
### 方法关键点
- 范式定义：平台用本地数据输出初排Top-K，用户侧个人Agent仅能拿到初排结果、物品元数据和授权的跨平台历史，选择性调整排序输出最终结果，核心目标是最大化救回平台漏判的内容，最小化覆盖平台正确排序的伤害
- 基准MediateRec：构建两类评测环境，一是用亚马逊不同品类作为代理跨平台场景，二是用Steam/任天堂/Xbox真实跨平台行为数据集OpenPlay，严格控制信息边界：平台看不到跨平台历史，Agent看不到平台内部模型和全局协同数据
- 训练方法PAMO：基于GRPO优化，通过反事实mask跨平台历史，对比相同推理逻辑在有无跨平台历史下的输出概率差，计算「个人介导支持度」，衡量排序调整是否真的依赖跨平台历史；按排名分层计算优势，加价值地板约束，将奖励优先分配给确实使用跨平台历史且效果好的调整，避免无依据乱改
### 关键结果
在5个测试集上，PAMO训练的4B开源模型比纯GRPO基线HR@10平均提升1.8%，NDCG@10平均提升0.018，有害覆盖率平均降低15%，效果超过Claude Opus零样本表现；72%的救回案例的调整依据明确来自跨平台历史，而非随机重排。

最值得记住的结论：用户侧个人Agent做推荐的核心不是比平台排得更好，而是在尊重平台全局协同信号的基础上，仅在有明确跨平台历史依据时才调整排序，平衡增益与伤害。
