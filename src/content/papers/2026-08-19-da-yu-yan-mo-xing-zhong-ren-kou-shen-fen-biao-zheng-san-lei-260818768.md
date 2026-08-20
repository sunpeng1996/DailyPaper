---
title: 'Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity
  in a Language Model'
title_zh: 大语言模型中人口身份表征三类可解离性质的实证研究
authors:
- Fathin Difa Robbani
affiliations:
- Independent Researcher
arxiv_id: '2608.18768'
url: https://arxiv.org/abs/2608.18768
pdf_url: https://arxiv.org/pdf/2608.18768
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: 大模型可解释性 · 人口身份表征研究
tags:
- LLM Interpretability
- Representational Similarity Analysis
- Probing
- Causal Intervention
- Demographic Representation
one_liner: 通过表征相似性分析定位LLM人口身份忠实表征位点，证实可读/忠实/因果使用三者独立
practical_value: '- 做用户persona模拟的业务（如电商用户调研、营销文案人群定向），不要依赖LLM表层输出的群体差异，优先从中间层高忠实度attention
  head做探针读取群体偏好，准确率比直接生成高21-31%

  - 人群标签体系设计参考：政治/社会经济属性的LLM内部表征更稳定，种族/宗教相关属性表征脆弱且对prompt敏感，业务中对后者的人群分层不要过度依赖LLM能力

  - 做LLM群体模拟微调时，无需重复学习模型已内部编码的群体结构，可直接基于忠实表征位点做轻量对齐，降低微调成本同时避免迁移退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM被广泛用于模拟受访用户生成调研结果，但输出同质化严重，无法如实反映真实群体间的意见差异。过往研究要么仅做黑盒效果评估，要么仅解码内部表征但未对齐真实人群ground truth，无法明确失效根源是模型未学到真实群体结构，还是学到了但推理时未调用。
### 方法关键点
- 以Pew美国趋势面板169个交叉人口群体（覆盖年龄×党派、教育×收入、种族×宗教等6类组合）的真实回答分布为ground truth，构建群体间意见距离矩阵
- 对Mistral-7B的1089个读出口（每层残差流、每个attention head输出、每个FFN输出）做表征相似性分析（RSA），以内部表征群体距离矩阵和真实意见矩阵的Spearman相关性为忠实度得分
- 结合激活补丁因果干预实验，验证不同位点表征是否被模型用于生成回答
### 关键结果
- Attention head忠实度显著优于残差流读出口，选择校正后最高ρ达0.63，达测量可靠性上限的70%；固定位点L11H16在全部6类属性上均有显著忠实度，种族相关属性表征普遍更弱且对prompt敏感
- 表征忠实度和因果使用无相关性：最清晰的因果路径出现在忠实度最低的属性类（p=0.002），最忠实的属性类无检测到的单层因果效应，替换prompt全量身份信息仅让预测偏移不到误差的2%
- 仅对L11H16做探针读取，结果比模型自身输出离真实调研结果近21-31%，但无法恢复单问题下的群体排序，表现与模型输出相当
### 核心结论
LLM内部对人口群体结构的编码能力、编码的忠实度、生成时的实际使用率是三个完全独立的属性，混为一谈是“LLM能否模拟人群”争议长期无解的核心原因
