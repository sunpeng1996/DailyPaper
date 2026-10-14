---
title: 'PAG-Agent: Zero-Shot Personalized Music Album Generation via Aesthetic Profile
  Distillation'
title_zh: PAG-Agent：基于审美画像蒸馏的零样本个性化音乐专辑生成
authors:
- Yifeng Mao
- Ziye Wang
- Yutong Shen
- Feiran Liu
- Wenjuan Han
affiliations:
- Beijing University of Technology
- Beijing Jiaotong University
arxiv_id: '2610.14508'
url: https://arxiv.org/abs/2610.14508
pdf_url: https://arxiv.org/pdf/2610.14508
published: '2026-10-10'
collected: '2026-10-14'
category: GenRec
direction: 生成式推荐 · 多模态偏好蒸馏
tags:
- Personalized Generation
- Multimodal LLM
- Aesthetic Profile
- Zero-Shot
- Evaluation Metric
one_liner: 提出PAG-Agent多模态框架，通过审美画像蒸馏实现零样本个性化音乐专辑生成
practical_value: '- 做个性化生成式推荐时，可复用「用户行为→显式结构化偏好画像→生成控制指令」的解耦架构，无需微调生成底座即可适配不同下游生成模型，零样本落地门槛低，适合定制化内容生成、商品营销文案生成等场景

  - 个性化效果评估可参考ACS+ASI双指标设计，既衡量目标用户匹配度，又排除大众通用内容的干扰，解决传统评估只看平均满意度的缺陷，尤其适配内容推荐、千人千面营销场景

  - 多模态偏好建模可结合用户行为（历史消费/浏览内容）+ 结构化属性（人口/兴趣标签）双输入，实验证明两者结合比单模态输入的个性化准确度提升14%以上，可直接复用在用户画像升级场景'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
当前Large Music Models (LMM)仅优化群体级质量与显式可控性，未覆盖用户个性化审美偏好匹配需求，直接输入用户行为的生成方式存在偏好表达模糊、通用内容占比高的问题，同时缺乏同时衡量用户匹配度和个性化独特性的评估体系，无法有效验证生成内容的个性化效果。

### 方法关键点
- 架构解耦为两个模块：多模态LLM蒸馏模块从用户喜欢的歌曲音频+上下文属性（年龄、职业、MBTI等）生成JSON格式的结构化个人审美画像，包含审美总结、核心风格属性、负向约束三类信息；规划LLM将画像转换为生成器可识别的曲目级控制指令，可适配任意音乐生成底座
- 配套PA-Eval评估体系：定义6维审美空间（情感效价、能量唤醒度、声音纹理复杂度等），设计两个核心指标：ACS（审美一致性得分）衡量生成内容和目标用户偏好的匹配度，ASI（审美特异性指数）扣除生成内容匹配其他用户的部分，避免「大众讨喜」内容的假高得分

### 关键实验
基于自建的100用户Personal-100数据集，对比Random（无用户信息通用提示）、Direct（直接输入用户信息不生成中间画像）两个baseline，跨Gemini/GPT底座、Suno-V5/ACE-Step生成器的所有配置下，PAG-Agent的ACS较Direct提升9~19%、ASI提升27~29%，较Random提升33~37% ACS、46~54% ASI；50人用户调研显示ACS和主观偏好的相关系数r=0.64，同时生成内容的通用音乐质量和baseline无显著差异。

### 核心结论
个性化生成的核心不是生成质量最高的内容，而是生成既匹配目标用户偏好、又不会同时适配大多数人的专属内容，显式结构化的中间偏好画像能同时提升生成可控性和效果可解释性。
