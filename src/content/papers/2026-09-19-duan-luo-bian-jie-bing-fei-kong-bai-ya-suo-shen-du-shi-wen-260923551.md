---
title: Paragraph Boundaries Are Not White Space:Compression Depth as the Signature
  of Hierarchical Structure
title_zh: 段落边界并非空白：压缩深度是文本层级结构的识别特征
authors:
- Shuyang Xiang
arxiv_id: '2609.23551'
url: https://arxiv.org/abs/2609.23551
pdf_url: https://arxiv.org/pdf/2609.23551
published: '2026-09-19'
collected: '2026-09-28'
category: LLM
direction: 大模型位置编码 · 文本层级结构建模
tags:
- hRoPE
- Positional Encoding
- Attention Compression
- Text Hierarchy
- RoPE
one_liner: 通过层级旋转位置编码hRoPE验证，压缩深度是真实段落层级结构的可复现核心标识
practical_value: '- 处理长文本（商品详情页、用户评价聚合、多轮对话历史）时可引入hRoPE分层位置编码，强化段落/会话层级的注意力边界感知，提升长上下文理解准确率

  - 做文本结构检测（商品评价观点分层、客服对话意图切换识别）时，可将跨边界注意力压缩深度作为特征，比传统嵌入一致性特征的判别性更强

  - 长文RAG召回后做上下文拼接时，可通过hRoPE显式标注不同来源检索块的层级坐标，减少跨块无关注意力干扰，提升RAG回答准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统1维位置编码仅建模阅读顺序，无法捕捉文本的段落、句子层级结构，不能解释相同token序列不同分段下的注意力差异，也缺乏量化真实层级结构的可复现指标。

### 方法关键点
提出层级旋转位置编码hRoPE，将段落、句子、token索引作为独立通道建模位置；固定token序列仅修改段落坐标，设计token距离精确的estimator度量跨段落注意力；对比真实分段和密度匹配的随机分段对照组的注意力压缩效果，同时对比词汇持久性、段落长度、嵌入一致性三类共8种语料特征的效果。

### 关键结果数字
真实段落结构的注意力压缩深度显著高于随机对照组，且压缩深度随语料差异变化，对照组无该特性；现有8种语料特征均无法完全复现压缩深度的跨语料排序，仅嵌入一致性特征最接近，压缩深度是真实段落结构的唯一可复现标识。
