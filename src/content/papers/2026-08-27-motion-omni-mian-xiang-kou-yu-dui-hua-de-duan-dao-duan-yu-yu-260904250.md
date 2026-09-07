---
title: 'Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue'
title_zh: Motion-Omni：面向口语对话的端到端语音与全身动作联合生成框架
authors:
- Chengqian Ma
- Wei Tao
- Haoyu Zhang
- Yiwen Guo
affiliations:
- Peking University
- LIGHTSPEED
- The Chinese University of Hong Kong, Shenzhen
- Independent Researcher
arxiv_id: '2609.04250'
url: https://arxiv.org/abs/2609.04250
pdf_url: https://arxiv.org/pdf/2609.04250
published: '2026-08-27'
collected: '2026-09-07'
category: Multimodal
direction: 多模态数字人 · 语音动作联合生成
tags:
- Multimodal-LLM
- End-to-End-Generation
- Digital-Human
- Dialogue-System
- Low-Latency
one_liner: 提出端到端多模态口语对话框架，同步生成语音与匹配全身动作，推理速度提升5.4倍
practical_value: '- 端到端多模态联合训练范式可直接迁移到电商直播数字人场景，替代级联方案降低两次推理的延迟开销，同时提升话术与动作的对齐度

  - 用可替换领域专家模型生成伪标注的pipeline可复用在缺少多模态对齐标注的业务场景（如带货话术+演示动作匹配），大幅降低标注成本

  - 从LLM隐层直接分支输出多模态结果的架构，可借鉴到同时生成推荐文案+商品演示素材的多模态推荐场景，提升内容一致性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有口语对话与配套动作生成采用级联方案，需两次完整推理，延迟高，且无法联合优化导致语音与动作对齐度差。
### 方法关键点
1. 端到端框架基于Qwen2.5-7B-Instruct backbone，从生成语音的LLM隐层直接输出人脸表情、四肢全身动作，无需依赖生成后的音频；
2. 联合训练LLM、语音生成器、动作生成器，避免冻结语音分支导致的对齐问题，同时保留原有对话能力；
3. 用可替换动作教师模型生成伪标注，得到422856条质量排序的语音-动作对（共1402小时），配套发布SwDA-500数据集与首个开放域全身口语对话统一评估协议。
### 关键结果
推理速度比级联方案快5.4倍（RTF=0.78，快于实时），无参考动作指标仅比同音频教师级联方案低2%，词错误率2.62%为参比多模态系统最低，beat相关性和多样性超过所有非教师级联方案。
