---
title: 'The Vocabulary Tax: Safely Trimming Unused Tokens from LLMs for On-Device
  Use'
title_zh: 词汇税：面向端侧部署的LLM未使用token安全裁剪方法
authors:
- Sattaya Singkul
affiliations:
- Independent Researcher, Bangkok, Thailand
arxiv_id: '2611.19913'
url: https://arxiv.org/abs/2611.19913
pdf_url: https://arxiv.org/pdf/2611.19913
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: LLM端侧优化 · 词表安全裁剪
tags:
- LLM Compression
- On-Device LLM
- BPE
- Vocabulary Pruning
- Edge AI
one_liner: 提出带合并闭包的BPE词表裁剪方法和免测试集的裁剪证书，大幅降低端侧LLM内存占用
practical_value: '- 端侧部署垂直领域Agent/电商推荐助手时，可直接复用开源的ai-model-explorer工具裁剪词表，无需微调即可降低4.4%~29%的模型体积，适配边缘设备内存限制

  - 垂直场景LLM微调前可先做合并闭包的词表裁剪，仅保留业务语料覆盖的token，既降低训练显存占用，又不会出现BPE拆分错误导致的效果下降

  - 可借鉴Good-Turing裁剪证书的思路，无需预留测试集就能预判词表裁剪后的token拆分错误率，提前评估业务效果损耗

  - 多语言电商/全球化推荐场景，可基于书写系统规则快速裁剪词表，默认保留拉丁字符避免跨语言借词/编码错误，词表拆分一致性可达100%'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
开源多语言LLM词表最大可达262k，输入嵌入、非绑定输出头、端侧模型的层嵌入都会随词表线性占用内存，单语言/少语言部署时大量未使用token造成的「词汇税」对小参数端侧模型影响尤其严重；传统基于语料频率的裁剪方法会破坏BPE合并规则，导致实际文本拆分错误率是标称值的1.9倍，且无法提前预判效果损耗。

### 方法关键点
- 两类词表保留规则：书写系统规则保留目标语言字符+通用/继承字符+默认拉丁字符，保证目标语言文本拆分100%与原模型一致；语料频率规则额外保留业务语料中出现的token，进一步压缩词表体积
- 合并闭包修复：递归保留所有保留token的BPE合并父节点，解决传统裁剪导致的保留token不可达问题，仅多保留5.9%的token即可将实际拆分错误率降到标称值的0.94倍
- 裁剪证书：基于Good-Turing估计和Heaps定律，仅用裁剪语料就能估算新文本的拆分错误率，以及达到目标错误率需要的语料量，无需额外测试集

### 关键结果
测试覆盖1244个Hugging Face生成/语音模型、22种语言，对比传统词表裁剪方法：
1. 0.5B以下小模型词汇税中位数为4.4%，用语料裁剪+合并闭包可额外移除29%的模型字节，拆分错误率低于2%的情况下最多可移除89.7%的词表行
2. 裁剪证书估算拆分错误率的相关系数达0.996，误差仅4.5%~6.6%，远优于留验证集方案的23%~27%误差
3. 裁剪后模型比特每字符上升不超过2.0%，93%以上的生成结果与原模型完全一致

> 最值得记住的一句话：多语言LLM的词汇税是累退的，参数越小的端侧模型受影响越严重，带合并闭包的词表裁剪可以在几乎不损失效果的前提下大幅降低端侧部署成本。
