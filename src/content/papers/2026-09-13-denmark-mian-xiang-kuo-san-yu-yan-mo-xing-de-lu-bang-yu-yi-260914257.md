---
title: 'DenMark: Robust Semantic Watermarking for Diffusion Language Models'
title_zh: DenMark：面向扩散语言模型的鲁棒语义水印框架
authors:
- Tianhao Ma
- Weihao Xuan
- Dong-Dong Wu
- Farshid Nooshi
- Takashi Ishida
- Gang Niu
- Naoto Yokoya
- Masashi Sugiyama
affiliations:
- The University of Tokyo
- RIKEN Center for Advanced Intelligence Project
arxiv_id: '2609.14257'
url: https://arxiv.org/abs/2609.14257
pdf_url: https://arxiv.org/pdf/2609.14257
published: '2026-09-13'
collected: '2026-09-15'
category: LLM
direction: 扩散大模型 · 语义水印
tags:
- Diffusion Language Model
- Semantic Watermark
- Watermark Detection
- LLM Security
- Text Generation
one_liner: 提出适配扩散语言模型的语义水印框架DenMark，全测试场景下检测指标均达最优
practical_value: '- 生成式电商营销内容溯源：可复用DenMark的语义水印注入逻辑，在DLM生成的商品描述、营销文案、Agent交互回复中嵌入隐式水印，防范篡改和版权纠纷

  - 语义篡改场景检测：可复用其候选单元尺寸校准扫描的检测方法，应对改写、paraphrase等攻击下的水印识别，适配UGC/AI生成内容的合规校验

  - 非自回归生成任务水印注入：针对批量生成搜索query、商品标题等非自回归生成任务，可借鉴临时rollout语义预估计的trick，在生成中间态完成水印嵌入，不影响生成质量'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语义水印方案均针对自回归大模型（ARLM）设计，无法适配扩散语言模型（DLM）迭代去噪、token灵活更新的生成范式，DLM生成内容缺乏鲁棒的语义防伪、溯源能力。
### 方法关键点
1. 直接在DLM去噪过程中注入密钥关联信号，将输出划分为固定token区域，通过临时rollout做语义前瞻，估计未完成区域的最终语义，选择高水印得分的局部更新，迭代累积水印信号；
2. 检测阶段对候选单元尺寸做校准扫描，抵御语义攻击带来的边界偏移问题。
### 关键结果
在4个DLM backbone、3个数据集、4种语义攻击的共48组测试组合中，所有检测指标均达到最优水平。
