---
title: 'Penquiry: A Pen-based Interactive In-situ Q&A System Leveraging LLMs'
title_zh: Penquiry：基于大语言模型的笔式交互式原位问答系统
authors:
- Jeongmin Rhee
- Changhee Lee
- Hyunwoo Kim
- Kiroong Choe
- Bohyoung Kim
- Sungahn Ko
- Jinwook Seo
affiliations:
- Seoul National University
- Pohang University of Science and Technology
- Hankuk University of Foreign Studies
arxiv_id: '2609.19870'
url: https://arxiv.org/abs/2609.19870
pdf_url: https://arxiv.org/pdf/2609.19870
published: '2026-09-17'
collected: '2026-09-20'
category: LLM
direction: LLM多模态交互式输入优化
tags:
- LLM
- Multimodal Input
- Q&A
- Interactive Interface
- User Experience
one_liner: 提出笔式输入适配的LLM原位问答系统，通过两层交互机制降低学习场景提问成本
practical_value: '- 多模态交互场景可借鉴Content Snapping机制，解决用户非结构化输入（如手绘圈选商品/评论内容）的指代消歧问题，降低用户交互成本

  - 稀疏输入补全方案可复用在搜索场景，将用户手绘标注、零散关键词自动补全为完整语义query，提升意图识别准确率

  - 原位交互范式可迁移到电商导购Agent，支持用户在商品详情页直接圈选提问，无需跳转对话窗口，提升转化效率'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
笔式数字设备是高认知参与度学习的主流介质，但现有LLM问答高度依赖键盘输入，与笔式空间化、非结构化的输入workflow存在交互鸿沟，用户提问面临两大核心障碍：一是细粒度视觉元素（公式/图表）难对齐到query上下文的指代障碍，二是非文本意图需要转写为结构化文本的表达障碍，手写长query还会额外增加用户负担。
### 方法关键点
新增笔输入到LLM的中介交互层：1）Content Snapping：将用户手绘圈选内容与邻近文档文本元素自动对齐，消除指代歧义；2）Question Autocompletion：将稀疏手写关键词扩展为语义完整的LLM可解析query，无需用户完整输入长问句。
### 关键结果
两轮迭代用户研究（每轮N=16）验证，相比传统键盘交互界面，该系统可显著降低用户提问的认知与物理开销
