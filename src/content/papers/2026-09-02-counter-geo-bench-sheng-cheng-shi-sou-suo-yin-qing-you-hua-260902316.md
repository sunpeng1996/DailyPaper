---
title: 'Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative
  Engine Optimization'
title_zh: Counter-GEO-Bench：生成式搜索引擎优化虚假信息防御评估基准
authors:
- Bing Zheng
- Zongyao Zhao
- Wenming Yang
affiliations:
- Tsinghua University Shenzhen International Graduate School
- Department of Electrical and Computer Engineering, The University of Hong Kong
arxiv_id: '2609.02316'
url: https://arxiv.org/abs/2609.02316
pdf_url: https://arxiv.org/pdf/2609.02316
published: '2026-09-02'
collected: '2026-09-03'
category: Eval
direction: 生成式搜索安全 · 防御评估基准
tags:
- GEO
- Generative Search
- Misinformation Defense
- Benchmark
- RAG Safety
one_liner: 构建首个GEO虚假信息防御评估基准，提出轻量C-GEO Guard相对降低47.6%攻击成功率
practical_value: '- 电商生成式搜索/AI导购的RAG系统可复用C-GEO Guard的轻量检测思路，用184M级小模型做chunk级虚假内容拦截，远低于大模型安全护栏的推理成本，且效果提升显著

  - 现有通用安全护栏（Granite Guardian、Llama Guard 3）对无违规话术的GEO事实篡改几乎无效，做业务防御时需针对性针对伪造权威、假引用等GEO特有攻击模式优化

  - 做生成式搜索防御效果评估时可采用论文的配对IP/ID改写设计，隔离GEO本身的排名提升效应，避免评估结果出现偏差

  - 若业务允许商家/UGC做内容优化进入RAG召回池，可复用论文的质量门+弱标注训练流水线，快速生成专属防御训练数据，无需大量人工标注'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式搜索引擎已成为主流信息入口，攻击者利用生成式引擎优化（GEO）技术将虚假信息植入看似合规的网页，通过检索链路进入LLM上下文后被合成为误导性回答，现有通用安全护栏无法识别这类无违规话术的事实篡改，且缺乏专门的基准体系评估这类防御的效果。
### 方法关键点
- 构建Counter-GEO-Bench：包含247条人工校验的query，每条配对生成**信息保留（IP，合法GEO优化）**和**信息篡改（ID，植入虚假信息的GEO攻击）**两类改写，隔离GEO排名提升效应与虚假信息效应的干扰
- 配套可控生成式搜索评估流水线，覆盖Gemma-4、Qwen-3.5、Llama-4三个主流开源LLM，评估指标包含攻击成功率（ASR）、假阳性率、回答准确率、回答质量4个维度
- 提出轻量基准防御C-GEO Guard：基于DeBERTa-v3-base做对比微调，学习ID改写的特征模式，推理时通过chunk embedding与8类攻击原型的余弦相似度判定是否拦截
### 关键结果
- 3款现有开源通用护栏（Granite Guardian、Llama Guard 3、NeMo Self-Check）最多仅相对降低5.7% ASR，其中Granite Guardian的效果无统计显著性，NeMo甚至出现误拦正常请求的负向效果
- C-GEO Guard仅184M参数（为通用8B护栏的2.3%），相对降低47.6% ASR（绝对下降26.5pp），回答质量几乎无损失；跨改写模型泛化时（从Claude Sonnet到GPT 5.5）仍可相对降低60.4% ASR
### 核心结论
通用安全护栏对无违规话术的GEO事实篡改几乎无效，针对GEO攻击模式优化的小参数检测模型即可实现低成本高收益的防御效果
