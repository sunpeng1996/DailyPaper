---
title: 'Universal Byte-Level Encoding: UTF-8/UTF-16 Routing to Reduce Cross-Script
  Token-Budget Disparities'
title_zh: 通用字节级编码：通过UTF-8/16路由降低跨脚本token预算差异
authors:
- Hyunsik Kim
- Youngmoon Jung
affiliations:
- Samsung Research
arxiv_id: '2610.01984'
url: https://arxiv.org/abs/2610.01984
pdf_url: https://arxiv.org/pdf/2610.01984
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: 多语言LLM · 分词效率优化
tags:
- Tokenizer
- Multilingual LLM
- BBPE
- Token Efficiency
- UTF Encoding
one_liner: 提出双编码路由的UBE分词器，降低跨语言token预算差异且不损失LM性能
practical_value: '- 多语言Agent/电商推荐系统涉及CJK、小语种内容时，可替换现有BBPE为UBE，同等token预算下低资源语言上下文容量最高提升53%，还可降低prompt处理延迟

  - 电商多语言商品标题、用户评论的LLM处理场景，UBE完全兼容现有BPE训练逻辑，仅需替换前后置编码模块，无需修改模型架构，迁移成本极低

  - 端侧轻量LLM（32K-64K词表）的多语言AI导购、推荐解释场景下，UBE降低跨语言token差异的收益最明显，还可与SuperBPE、SCRIPT-BPE等边界优化策略叠加使用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有UTF-8基础的BBPE分词器存在严重跨脚本token预算差异：CJK等3字节BMP字符的编码floor为3，是英文的3倍，低资源语言相同语义内容消耗token数最高可达英文15倍，导致固定上下文窗口下有效内容容量低、推理成本高；统一替换为UTF-16编码又会抬升英文token消耗，混合脚本场景收益为负。
### 方法关键点
- 设计逐字符双编码路由规则：字符UTF-8编码长度≤2走UTF-8路径，≥3走UTF-16路径，无需语言检测，仅修改BPE输入符号流
- 用UTF-8原生256字节表+UTF-16专用PUA区256字节表构成512个基础符号，无额外标记token，保证完全可逆解码
- 100%兼容标准BPE合并逻辑、各类边界策略、形态学表示方案，无需修改Transformer模型架构
### 关键实验结果
基于FLORES-200、mC4多语言语料测试，对比BBPE、BBPE16及主流开源LLM分词器：
- 101种语言32K词表设置下，token溢价Gini系数降低9.4%，低资源3字节脚本token数最高降34.7%，英文token数微降0.3%
- 182M多语言LM训练中，UBE与BBPE下游任务性能完全持平，同内容prompt处理速度对Amharic提升45%、英文提升3.9%
- 可与SuperBPE、SCRIPT-BPE、MYTE等分词优化方案叠加使用，均能进一步降低token消耗

> 最值得记住的结论：16K-64K词表的轻量多语言LLM场景下，UBE仅付出<1%的词表开销即可大幅降低跨语言token预算差异，且无性能损失
