---
title: 'KUAISHOU Explorer LLM-Rec Challenge 2026: Reasoning Generative Recommendation'
title_zh: 2026快手Explorer LLM-Rec挑战赛：推理型生成式推荐技术报告
authors:
- Jiangxia Cao
- Hao Peng
- Wenlong Xu
- Jiaxin Deng
- Zhixin Ling
- Xingmei Wang
- Kun Shang
- Can Tang
- Zhihuai Cai
- Jun Du
affiliations:
- Kuaishou
- SIGIR 2026
arxiv_id: '2609.39828'
url: https://arxiv.org/abs/2609.39828
pdf_url: https://arxiv.org/pdf/2609.39828
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式推荐 · 推理型多域生成推荐
tags:
- Generative Recommendation
- Semantic ID
- Chain-of-Thought
- Multi-domain Recommendation
- LLM4Rec
one_liner: 公开推理型生成式推荐的多域工业数据集、评测基准及头部竞赛方案
practical_value: '- 多域生成推荐落地可复用四级粒度（token/item/relation/user）的Semantic ID与自然语言对齐预训练方案，能大幅提升生成结果的语义一致性

  - 引入推理轨迹做SFT时，可仅对推理文本计算loss、屏蔽最终SID的loss，有效提升think与nothink模式的候选互补性，避免推荐多样性下降

  - 多场景生成推荐无需强制统一推理格式，可根据场景特性选择是否启用推理（如电商用think、短视频用nothink），效果优于全场景统一配置

  - 分层结构的Semantic ID生成可采用分级奖励+分层信用分配方案，解决仅奖励完整命中时浅层代码优先的问题，提升全码命中率'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐引入CoT推理时常出现性能不升反降的问题，行业缺乏统一的推理型生成推荐评测基准与工业级多域数据集，难以支撑推荐大模型的规模化迭代。

### 方法关键点
- 基座采用OneReason系列模型，基于Qwen-3扩展Semantic ID词表，通过token/item/relation/user四级粒度预训练实现物品、行为、自然语言的语义对齐，预训练总token量超500B
- 竞赛设置四大核心任务：物品理解（SID与描述双向映射）、用户理解（相关行为选择+兴趣演化链生成）、跨域推荐（think+nothink双模式生成候选SID）、常识理解，覆盖推荐大模型全能力维度
- 公开资源包含：94万+SFT样本（41万+带CoT轨迹）、50万匿名用户多域（短视频/电商/广告/直播）交互序列、3591万+物品的SID-描述映射表、统一评测基准
- 头部核心优化：冠军采用自采样推理+目标SID掩码训练；亚军采用分域选择推理格式的多任务SFT；季军采用分阶段RL+DPO偏好优化；创新方案提出前缀引导+分层信用分配优化分层SID生成

### 关键结果
竞赛共吸引2031名开发者、1206支队伍参赛，冠军方案总得分1.44，较基线提升超30%；think与nothink双模式融合的Pass@32较单模式提升15%以上；分域推理配置较全场景统一配置提升8%左右。

### 核心结论
推理式生成推荐的核心不是强制引入CoT，而是要通过语义对齐、推理监督设计、分域适配让推理过程真正服务于推荐效果，而非单纯提升推理文本的通顺度。
