---
title: 'Present but Hard to Read: Probing Latent Reasoning with Minimal Pairs'
title_zh: 存在但难读取：用最小对方法探测大模型潜在推理
authors:
- Aur Shalev Merin
affiliations:
- Independent Researcher
arxiv_id: '2610.28498'
url: https://arxiv.org/abs/2610.28498
pdf_url: https://arxiv.org/pdf/2610.28498
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM可解释性 · 隐状态探测
tags:
- Probing
- Latent Reasoning
- Interpretability
- Looped Transformer
- Minimal Pairs
one_liner: 发现大模型隐状态存在标准探针读不到的特征，提出严谨的潜在推理探测协议
practical_value: '- 做LLM4Rec的用户/商品特征隐状态校验时，不要仅凭标准线性探针读不到就判定特征未被模型编码，可构造最小对（同上下文仅修改目标特征）做对照验证，避免误判

  - 做推理类Agent的内部状态监控、特征干预时，需补充activation patching类因果验证，不要直接把探针的读取结果等同于特征对推理的实际作用，避免对冗余特征做无效干预

  - 若需在业务中探测大模型的隐式计算结果，可复用文中的探测协议框架：先加copy特征的baseline，再用符号翻转、素数模对照排除偶然相关性，提升探测结果的可信度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
过往潜在推理探测研究普遍将标准探针的阴性结果作为特征不存在的证据，该假设未被严格验证，尤其对looped transformer这类主打隐式思考的模型，解读偏差会误导对其推理能力的判断。
### 方法关键点
- 对比两类探针：标准单样本探针（仅输入单个prompt的隐状态）、最小对探针（同模板仅修改目标特征，减去组均值后探测）
- 测试覆盖looped架构Ouro-1.4B与标准Transformer Qwen2.5-1.5B，以GSM8K算术题为测试场景
- 提出多步校验的探测协议：包含copy上限、素数模对照、全输入组合排序、符号翻转孪生对照、输出混合校验，结合patching验证特征是否被实际用于推理
### 关键结果
- 最小对探针对输入数字的读取准确率达0.9左右，而标准单样本探针即便用5249条训练样本，在Ouro上准确率仅0.36，Qwen上仅0.19
- 特征难读取的原因是信号幅度小而非方向拥挤，即使是无关输入的特征也会留下可被最小对探针检测到的痕迹
- 对Ouro的两步算术题测试显示，隐状态中存在和中间计算结果`a+b`相关的弱信号，但patching替换该信号后不会改变模型输出，说明该特征可读但未被实际用于推理
### 核心结论
大模型隐状态里能被探针读到的特征不一定真的参与推理，探针读不到的特征也不一定不存在，探测结果的解读必须依赖严格的对照实验
