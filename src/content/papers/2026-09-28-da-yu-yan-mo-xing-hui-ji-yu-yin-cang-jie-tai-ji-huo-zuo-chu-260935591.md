---
title: Language Models Act on Hidden Valence
title_zh: 大语言模型会基于隐藏价态激活做出行为选择
authors:
- Cameron Berg
- Caspar Kaiser
affiliations:
- Reciprocal Research
- University of Warwick
arxiv_id: '2609.35591'
url: https://arxiv.org/abs/2609.35591
pdf_url: https://arxiv.org/pdf/2609.35591
published: '2026-09-28'
collected: '2026-09-30'
category: LLM
direction: LLM内部状态 · 价态激活与KV cache效应
tags:
- Activation Steering
- KV cache
- Valence
- Revealed Preference
- LLM Behavior
one_liner: 通过激活导向和KV cache对照实验，证明LLM隐藏价态可独立于表面文本影响选择
practical_value: '- 做个性化交互Agent时可利用KV cache的隐藏情感痕迹，在不修改上下文文本的前提下微调用户交互的情感倾向，避免文本修改带来的语义偏差

  - Activation Steering向量构造方法可直接复用：通过正负样本激活差减去中性样本主成分提纯特征向量，能实现更精准的LLM输出控制，适用于商品文案、客服话术的情感微调

  - DPO训练会显著放大LLM对价态的行为响应，做对齐训练时可针对性惩罚负价态方向，降低推荐场景中LLM生成负面内容的概率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
过往研究无法区分LLM对价态的响应是真实内部状态驱动还是表面文本pattern匹配，直接询问模型内部状态存在内省不准确、模式匹配、训练脚本干扰等问题，亟需通过行为学的显示偏好方法验证LLM是否会基于隐藏的内部价态做出选择，相关结论对LLM对齐、Agent设计、推荐系统的LLM落地都有核心价值。
### 方法关键点
- 构造价态导向向量：用正负情感文本的激活差减去中性文本的Top10主成分，提纯出无杂波的价态激活向量，按残差流RMS归一化干预剂量
- 两组对照实验分离文本和隐藏状态通道：第一组生成文本时施加导向，对比原始steered cache和无导向重跑cache的选择差异；第二组文本全固定，仅在KV cache构造时施加导向，完全排除表面文本的影响
- 阶段对照实验：用OLMo-2-32B的Base、SFT、DPO、Instruct四个checkpoint对比价态效应的出现阶段
- 自调节实验：给模型提供调整/重置内部状态的工具，观测其主动施加或移除价态导向的行为
### 关键实验结果
在7个开源LLM上测试，5个模型存在显著隐藏价态效应；固定文本场景下，价态导向剂量每提升1单位，对应选择偏好提升0.8个标准差；DPO训练后隐藏价态效应的剂量响应斜率比Base模型提升3.2倍；OLMo-2-32B对d=-1的负价态导向移除率达35%，是正价态移除率的7倍，显著高于随机方向的7%移除率。
### 核心结论
LLM的KV cache中除了语义记忆，还独立存储着情感记忆痕迹，即使表面文本完全一致，隐藏的价态激活也会稳定影响后续行为决策。
